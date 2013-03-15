'use strict';

/* Services */


angular.module('paliTipitaka.services', ['pali.services', 'pali.filters', 'pali.directives', 'pali.jqlext']).
  factory('resizableViews', ['$document', function($document) {
    var leftView, viewwrapper, arrow, separator, rightView;
    var startLeftViewWidth, startRightViewWidth, initialMouseX;

    function initViews(allContainerId, leftViewId, viewwrapperId, arrowId, separatorId, rightViewId) {
      leftView    = angular.element(document.getElementById(leftViewId));
      viewwrapper = angular.element(document.getElementById(viewwrapperId));
      arrow       = angular.element(document.getElementById(arrowId));
      separator   = angular.element(document.getElementById(separatorId));
      rightView   = angular.element(document.getElementById(rightViewId));

      var width = document.getElementById(allContainerId).offsetWidth;
      var leftViewWidth = 250; //px
      var viewwrapperWidth = 7; //px
      var rightViewWidth = width - leftViewWidth - viewwrapperWidth;

      // set default width
      leftView.css(   'width', leftViewWidth    + 'px');
      rightView.css(  'width', rightViewWidth   + 'px');
      viewwrapper.css('width', viewwrapperWidth + 'px');

      arrow.bind('click', function() {
        var lwidth = parseInt(leftView.css('width').replace('px', ''));
        var rwidth = parseInt(rightView.css('width').replace('px', ''));
        leftView.css('width', '0');
        rightView.css('width', lwidth + rwidth + 'px');
      });

      separator.bind('mousedown', function($event) {
        $event.preventDefault();
        startLeftViewWidth = parseInt(leftView.css('width').replace('px', ''));
        startRightViewWidth = parseInt(rightView.css('width').replace('px', ''));
        initialMouseX = $event.clientX;
        $document.bind('mousemove', mousemove);
        $document.bind('mouseup', mouseup);
        return false;
      });
    }

    function mousemove($event) {
      // calculate the delta of mouse cursor movement
      var dx = $event.clientX - initialMouseX;

      var newlw = startLeftViewWidth + dx;
      if (newlw < 0) {
        leftView.css('width', '0');
        rightView.css('width', startLeftViewWidth + startRightViewWidth + 'px');
        return false;
      }

      var newrw = startRightViewWidth - dx;
      if (newrw < 0) {
        leftView.css('width', startLeftViewWidth + startRightViewWidth + 'px');
        rightView.css('width', '0');
        return false;
      }

      leftView.css('width', newlw + 'px');
      rightView.css('width', newrw + 'px');
      return false;
    }

    function mouseup() {
      $document.unbind('mousemove', mousemove);
      $document.unbind('mouseup', mouseup);
    }

    var serviceInstance = { initViews: initViews };
    return serviceInstance;
  }]).

  factory('htmlDoc2View', ['paliString', function(paliString) {
    /**
     * wrap all words in the element
     * @param {DOM element} FIXME: is this HTML or XML dom element?
     */
    function wrapWordsInElement(xmlElement) {
      // 1: element node
      if (xmlElement.nodeType == 1) {
        for (var i=0; i<xmlElement.childNodes.length; i++)
          // recursively call self to process
          wrapWordsInElement(xmlElement.childNodes[i]);
        return;
      }

      // 3: text node
      if (xmlElement.nodeType == 3) {
        var string = xmlElement.nodeValue;
        if (string.replace(/\s*/, '') !== '')
          // string is not whitespace
          xmlElement.parentNode.replaceChild(paliString.toDom(string), xmlElement);
        return;
      }

      console.log('In end of wrapWordsInElement: ');
      console.log(xmlElement);
    }

    function getView(htmlDoc) {
      /* cloneNode() is important. otherwise the second time nothing will show up */
      var body = htmlDoc.getElementsByTagName('body')[0].cloneNode(true);
      for (var i=0; i<body.childNodes.length; i++) {
        wrapWordsInElement(body.childNodes[i]);
      }

      return angular.element(body);
    }

    var serviceInstance = { getView: getView };
    return serviceInstance;
  }]).

  factory('paliString', ['$rootScope', 'htmlString2Dom', 'tooltip', 'jqlext', 'tooltipHandler', 'paliIndexes',
                function($rootScope, htmlString2Dom, tooltip, jqlext, tooltipHandler, paliIndexes) {
    // when user's mouse hovers over words, delay a period of time before look up.
    var DELAY_INTERVAL = 1000; // ms

    function showShortExplanationInTooltip(rawWordSpanDom) {
      var tooltipPosition = {
        'left': (jqlext.offset(rawWordSpanDom).left + 'px'),
        'top': (jqlext.offset(rawWordSpanDom).top + rawWordSpanDom.offsetHeight + 'px')
      };

      var word = rawWordSpanDom.innerHTML.toLowerCase();
      tooltip.show(tooltipPosition, tooltipHandler.getLookingUp(word));

      tooltipHandler.get(word, $rootScope.setting).then(
         function(doms) {
           if (doms.attr('isAdjustRatio') === 'false')
             tooltip.show(tooltipPosition, doms, false);
           else
             tooltip.show(tooltipPosition, doms);
      }, function(reason) {
           tooltip.show(tooltipPosition, reason);
      });
      $rootScope.$apply();
    }

    function onWordMouseOver(e) {
      this.style.color = 'red';
      if (!$rootScope.setting.showTooltip) return;

      setTimeout(angular.bind(this, function() {
        // 'this' keyword here refers to raw dom element
        if (this.style.color === 'red') {
          // mouse is still on word
          showShortExplanationInTooltip(this);
        }
      }), DELAY_INTERVAL);
    }

    function onWordMouseOut(e) {
      this.style.color = '';
      if (!$rootScope.setting.showTooltip) return;

      setTimeout(angular.bind(this, function() {
        tooltip.hide();
      }), DELAY_INTERVAL);
    }

    function onWordDbclick(e) {
      var word = this.innerHTML.toLowerCase();
      if (!paliIndexes.isValidPaliWord(word)) return;
      var url = 'http://palidictionary.appspot.com/browse/' + word[0] + '/' + word;
      if ($rootScope.isDevServer) url += '?track=no';
      window.open(url);
    }

    function toDom(string) {
      // wrap all pali words in span
      var spanContainer = htmlString2Dom.string2dom(markInSpan(string));
      for (var i=0; i<spanContainer.childNodes.length; i++) {
        var node = spanContainer.childNodes[i];
        var tagName = node.tagName;
        if (tagName && tagName.toLowerCase() === 'span') {
          node.onmouseover = onWordMouseOver;
          node.onmouseout = onWordMouseOut;
          node.ondblclick = onWordDbclick;
        }
      }
      return spanContainer;
    }

    function markInSpan(string) {
      return string.replace(/[AaBbCcDdEeGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvYyĀāĪīŪūṀṁṂṃŊŋṆṇṄṅÑñṬṭḌḍḶḷ]+/g, '<span>$&</span>');
    }

    var serviceInstance = { toDom: toDom };
    return serviceInstance;
  }]).

  factory('htmlString2Dom', [function() {
    /**
     * @see http://stackoverflow.com/questions/3103962/converting-html-string-into-dom-elements
     * @see http://stackoverflow.com/questions/888875/how-to-parse-html-from-javascript-in-firefox
     */
    function string2dom(string) {
      var spanContainer = document.createElement('span');
      spanContainer.innerHTML = string;
      return spanContainer;
    }

    var serviceInstance = { string2dom: string2dom };
    return serviceInstance;
  }]).

  factory('tooltipHandler', ['$rootScope', '$compile', '$q', '$templateCache', 'paliJson', 'paliIndexes', 'palidic',
                      function($rootScope, $compile, $q, $templateCache, paliJson, paliIndexes, palidic) {
    // require 'pali.filters' module
    var scope = $rootScope.$new(true);
    // FIXME: bad practice!!! don't use $rootScope.setting here!!!
    scope.setting = $rootScope.setting;
    scope.shortDicName = palidic.shortName;
    scope.shortDicExp = palidic.shortExp;
    scope.wordUrl = function(word) {
      if (!angular.isString(word)) return;
      var url = 'http://palidictionary.appspot.com/browse/' + word[0] + '/' + word;
      if ($rootScope.isDevServer) url += '?track=no';
      return url;
    }
    var shortDicNameExps = $compile($templateCache.get('/partials/shortdicexp.html'))(scope);

    var lookingUp = $compile('<span>{{_("Looking up")}} <span style="color: GoldenRod;">{{currentSelectedWord}}</span> ...</span>')($rootScope);
    var noSuchWord = $compile('<span>{{_("No Such Word")}}</span>')($rootScope);
    var netErr = $compile('<span>{{_("Internet Connection Error")}}</span>')($rootScope);

    function getLookingUp(word) {
      $rootScope.currentSelectedWord = word;
      return lookingUp;
    }

    function getNoSuchWord() { return noSuchWord; }

    var possibleWordsDoms = $compile("<div isAdjustRatio='false'>" +
        '<div ng-repeat="possibleWord in possibleWords"><a href="{{wordUrl(possibleWord)}}" target="_blank">{{possibleWord}}</a></div>' +
      '</div>')(scope);

    function getShortDicExps(word, setting) {
      // TODO: pre-process word (toLowerCase() etc.) here
      scope.setting = setting;
      if (paliIndexes.isValidPaliWord(word)) {
        scope.currentSelectedWord = word;
        scope.isGuessedWord = false;

        return paliJson.get(word).then( function(jsonData) {
          // get jsonData successfully by xhr CORS
          scope.dicWordExps = jsonData;
          return shortDicNameExps;
        }, function(reason) {
          // fail to get word via xhr CORS
          return netErr;
        });
      } else {
        var possibleWords = paliIndexes.possibleWords(word);
        var deferred = $q.defer();
        if (possibleWords) {
          scope.possibleWords = possibleWords;
          deferred.resolve(possibleWordsDoms);
        } else {
          deferred.reject(noSuchWord);
        }
        return deferred.promise;
      }
    }

    var serviceInstance = {
      getLookingUp: getLookingUp,
      getNoSuchWord: getNoSuchWord,
      get: getShortDicExps
    };
    return serviceInstance;
  }]);
