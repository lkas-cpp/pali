# Pāḷi Tipiṭaka & Dictionary

## Set Up Development Environment

<i>REPO_DIR</i> below means the directory where you git clone this repository. <i>GAE_PYSDK_DIR</i> means the directory of [Google App Engine Python SDK](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python).

1. Run <b>REPO_DIR/common/pytools/setupdev.py</b> to set up [New Tong Wen Tang](http://tongwen.openfoundry.org/) library (translation between Traditional and Simplified Chinese on client side) and [Jianfan](https://code.google.com/p/python-jianfan/) library (translation between Traditional and Simplified Chinese on server side), and symbolic links.
```bash
    python REPO_DIR/common/pytools/setupdev.py
```

2. Install [Babel](http://babel.edgewall.org/) ([Download](http://ftp.edgewall.com/pub/babel/Babel-0.9.6.zip)) and [gaepytz](https://pypi.python.org/pypi/gaepytz) ([Download](https://pypi.python.org/packages/source/g/gaepytz/gaepytz-2011h.zip#md5=0f130ef491509775b5ed8c5f62bf66fb), [Google Code](http://code.google.com/p/gae-pytz/)) for [internationalization and localization with webapp2](http://webapp-improved.appspot.com/tutorials/i18n.html). After download, zip the package in the source code and put under <i>REPO_DIR/common/gae/libs/</i>. The two packages will be [zipimport](https://developers.google.com/appengine/articles/django10_zipimport)ed in the application.
```bash
    wget http://ftp.edgewall.com/pub/babel/Babel-0.9.6.zip
    wget https://pypi.python.org/packages/source/g/gaepytz/gaepytz-2011h.zip#md5=0f130ef491509775b5ed8c5f62bf66fb
    unzip Babel-0.9.6.zip
    unzip gaepytz-2011h.zip
    cd Babel-0.9.6/
    zip -r babel.zip babel/
    mv babel.zip REPO_DIR/common/gae/libs/
    cd ../gaepytz-2011h/
    zip -r pytz.zip pytz/
    mv pytz.zip REPO_DIR/common/gae/libs/
```

3. Create i18n files for production use:
```bash
    cd REPO_DIR/common/pytools/
    # create i18n files
    python i18nUtils.py pot
    python i18nUtils.py po
    python i18nUtils.py cn
    python i18nUtils.py mo

    # create JavaScript file ( REPO_DIR/common/app/js/locales.js ) of translated strings for client side
    python i18nUtils.py js
```

4. Download pictionary definition (download point [#1](http://online-dhamma.net/anicca/downloads/pali-dict-linux-web1.zip), or [#2](http://dhamma.zxff.net/downloads/pali-dict-linux-web1.zip), or [#3](https://github.com/siongui/data/raw/master/pali-dict-linux-web1.zip). Choose one of them to download) from [PCED](http://online-dhamma.net/anicca/pali-course/Pali-Chinese-English%20Dictionary.html).
  Put pali-dict-linux-web1.zip under <i>REPO_DIR/common/pytools/</i> and unzip it.
```bash
    mv pali-dict-linux-web1.zip REPO_DIR/common/pytools/
    cd REPO_DIR/common/pytools/
    unzip pali-dict-linux-web1.zip
```

5. Generate index files and compiled JavaScript file:
```bash
    cd REPO_DIR/common/pytools/
    python xml2jsonIndex.py
    python jsonIndex2group.py
    python buildJsonDeployDir.py

    # create JavaScript file ( REPO_DIR/common/app/js/dicPrefix.js ) of indexes of pali words for client side
    python dicPrefix2js.py
    # create compiled JavaScript files ( REPO_DIR/dictionary/app/all_compiled.js and REPO_DIR/tipitaka/app/all_compiled.js ) by Google Closure Compiler Service API
    python compile.py
```

6. Deploy on [Google App Engine (Python)](https://developers.google.com/appengine/docs/python/gettingstartedpython27/uploading): Before deployment, please modify the application name at the first line in <i><b>REPO_DIR/tipitaka/app.yaml</b></i>, <i><b>REPO_DIR/dictionary/app.yaml</b></i>, <i><b>REPO_DIR/common/pytools/app-engine-json/jsons0/app.yaml</b></i>, <i><b>REPO_DIR/common/pytools/app-engine-json/jsons1/app.yaml</b></i>, <i><b>REPO_DIR/common/pytools/app-engine-json/jsons2/app.yaml</b></i>, and <i><b>REPO_DIR/common/pytools/app-engine-json/jsons3/app.yaml</b></i>. 
```bash
    # deploy json files of dictionary
    cd GAE_PYSDK_DIR/
    ./appcfg.py update REPO_DIR/common/pytools/app-engine-json/jsons0/
    ./appcfg.py update REPO_DIR/common/pytools/app-engine-json/jsons1/
    ./appcfg.py update REPO_DIR/common/pytools/app-engine-json/jsons2/
    ./appcfg.py update REPO_DIR/common/pytools/app-engine-json/jsons3/
    rm -rf REPO_DIR/common/pytools/app-engine-json/jsons0/
    rm -rf REPO_DIR/common/pytools/app-engine-json/jsons1/
    rm -rf REPO_DIR/common/pytools/app-engine-json/jsons2/
    rm -rf REPO_DIR/common/pytools/app-engine-json/jsons3/

    # deploy dictionary
    ./appcfg.py update REPO_DIR/dictionary
    # deploy tipitaka
    ./appcfg.py update REPO_DIR/tipitaka
```

## Writing JavaScript Code ...

Remember to re-compile all JavaScript files before deployment or before testing the compiled file:

```bash
cd REPO_DIR/common/pytools/
python compile.py
```

## Development of i18n

Everytime strings in html files are marked to be translated, remember to re-generate i18n files and re-compile JavaScript files. A helper script named <b>i18nUtils.py</b> (located under <b>REPO_DIR/common/pytools/</b>) to automate the i18n jobs.

```bash
cd REPO_DIR/common/pytools/
# create POT from html files
python i18nUtils.py pot
# initialize PO files if not exist, or update POs files if exist.
python i18nUtils.py po
# after initialization, edit PO files and translate strings in PO files. Then
python i18nUtils.py cn
# the above command update zh_CN PO file from zh_TW PO file,
# so you do not have to manual translate (optional if you want to manually translate zh_CN PO file).
# then create MO files for server-side i18n
python i18nUtils.py mo
# create files for client-side i18n
python i18nUtils.py js
# re-compile all JavaScript files
python compile.py
```

# References

## i18n (to be updated)

Related links to enable i18n:
* [Internationalization and localization with webapp2](http://webapp-improved.appspot.com/tutorials/i18n.html)
* [How to enable {% trans %} tag for jinja templates?](http://stackoverflow.com/questions/8471455/how-to-enable-trans-tag-for-jinja-templates)
* [Extensions - Jinja2 2.7-dev documentation](http://jinja.pocoo.org/docs/extensions/)

### Enable i18n Using webapp2, jinja2, babel, and gaepytz

To enable i18n using webapp2, jinja2, babel, gaepytz. The following lines in [main.py](https://github.com/siongui/palidictionary/blob/master/main.py) is crucial:
```bash
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaepalilibs/babel.zip'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaepalilibs/pytz.zip'))

from webapp2_extras import i18n

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.join(os.path.dirname(__file__), 'app'),
                                    os.path.join(os.path.dirname(__file__), 'app/sympartials')]),
    extensions=['jinja2.ext.i18n'],
    variable_start_string='{$',
    variable_end_string='$}')

jinja_environment.install_gettext_translations(i18n)
```
The point is that zipimport babel and gaepytz which we install in advance. Then import i18n in webapp2_extras, enable i18n extension of jinja2, and install webapp2 i18n in jinja2.

To tell jinja2 to serve translalted strings, the strings in HTML files need to be marked like the following:
```bash
# If default variable start_string and end_stirng are used
{{_("string_to_be_translated")}}

# In our case, we use {$ and $} as start_string and end_string respectively
# to prevent collision with the notation of AngularJS interpolation
# so we need to wrap the string like the following
{$_("string_to_be_translated")$}
```

And in the http request handler, call <em>[i18n.get_i18n().set_locale()](http://webapp-improved.appspot.com/api/webapp2_extras/i18n.html#webapp2_extras.i18n.I18n.set_locale)</em> to specify the locale we want to serve. The following sample code demonstrates how:
```python
class MainPage(webapp2.RequestHandler):
  def get(self):
    template_values = {...}
    i18n.get_i18n().set_locale('zh_TW')

    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))
```
### Extract from HTML and Create POT

Related links to generate translation files (POT, PO, and MO files):
* [Internationalize A Python Application](http://wiki.maemo.org/Internationalize_a_Python_application)
* [Python localization made easy](http://www.supernifty.org/blog/2011/09/16/python-localization-made-easy/)

The default locale directory of webapp2_extras i18n is <b>REPO_DIR/locale/</b> and default domain is <b><i>messages</i></b> (see [webapp2_extras.i18n.default_config](http://webapp-improved.appspot.com/api/webapp2_extras/i18n.html#webapp2_extras.i18n.default_config) for details). In our repository, the html files to be localized are located under <b>REPO_DIR/app/</b>, texts to be translated are wrapped in <b><i> _("TEXT_TO_BE_TRANSLATED") </i></b>. Note that cannot use <b><i> _(' ') </i></b> to wrap texts, must use <b><i> _(" ") </i></b>. Otherwise <i>[xgettext](http://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html)</i> utility cannot recognize the texts and will not put them in POT file. After finishing wraping texts to be translated, we can use the following Python code to generate POT file:
```python
locale_dir = os.path.join(os.path.dirname(__file__), '../locale')
html_dir = os.path.join(os.path.dirname(__file__), '../app')

if not os.path.exists(locale_dir):
  os.makedirs(locale_dir)

cmd_xgettext = 'xgettext --no-wrap --from-code=UTF-8 --keyword=_ --output=%s/messages.pot `find %s -name *.html`' % (locale_dir, html_dir)
cmd_sed = 'sed -i "s/charset=CHARSET/charset=utf-8/g" %s/messages.pot' % locale_dir

os.system(cmd_xgettext)
os.system(cmd_sed)
```
<i>[xgettext](http://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html)</i> is the utility to generate POT file. HTML format is not supported format so <i>xgettext</i> will give warnings but still can generate POT file. See this Stack Overflow [question](http://stackoverflow.com/questions/1656174/gettext-for-html-or-latex) for reference.

### Initialize PO from POT

The next step is to initialize the PO files for each locale. <b><i>[msginit](http://www.gnu.org/software/gettext/manual/html_node/msginit-Invocation.html)</i></b> is responsible for creating a new PO file for a given locale. The PO file of a given <i>locale</i> in our application will be located under <b>REPO_DIR/locale/{{locale}}/LC_MESSAGES/messages.po</b>, where {{locale}} is the name of the locale. The following Python code can be used to call <i>msginit</i> to create a PO file for a given locale.
```python
def initLocalePO(locale):
  locale_dir = os.path.join(os.path.dirname(__file__), '../locale')
  potpath = os.path.join(locale_dir, 'messages.pot')
  popath = os.path.join(locale_dir, '%s/LC_MESSAGES/messages.po' % locale)

  if not os.path.exists(os.path.dirname(popath)):
    os.makedirs(os.path.dirname(popath))
  cmd_msginit = 'msginit --no-translator --input=%s --locale=%s -o %s' % (potpath, locale, popath)
  os.system(cmd_msginit)
```
Currently three locales are supported (en_US, zh_TW, zh_CN). After PO files are created, edit the PO files to translate texts.

### Create MO from PO

Final step is to create MO files to be used in production. One PO file has a corresponding MO file. The following Python code shows how to use <b><i>[msgfmt](http://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html)</i></b> to create MO file from a give po file. The MO file in our application will be located in the same directory as the source PO file ( in <b>REPO_DIR/locale/{{locale}}/LC_MESSAGES/messages.po</b> ).
```python
def formatMO(locale):
  locale_dir = os.path.join(os.path.dirname(__file__), '../locale')
  popath = os.path.join(locale_dir, '%s/LC_MESSAGES/messages.po' % locale)
  mopath = popath[:-2] + 'mo'

  cmd_msgfmt = 'msgfmt %s -o %s' % (popath, mopath)
  os.system(cmd_msgfmt)
```

### Merge PO files

Everytime strings are marked in html files, [msgmerge](http://www.gnu.org/software/gettext/manual/html_node/msgmerge-Invocation.html) ([reference](http://wiki.xfce.org/translations/msgmerge)) can be used to merge translated strings from two PO (or POT) files into one, so translated strings can be re-used without manual typing once again.
```python
def updateLocalePO(locale):
  locale_dir = os.path.join(os.path.dirname(__file__), '../locale')
  potpath = os.path.join(locale_dir, 'messages.pot')
  popath = os.path.join(locale_dir, '%s/LC_MESSAGES/messages.po' % locale)

  if not os.path.exists(os.path.dirname(popath)):
    os.makedirs(os.path.dirname(popath))
  cmd_msginit = 'msgmerge --no-wrap --backup=none --update %s %s' % (popath, potpath)
  print(cmd_msginit)
  os.system(cmd_msginit)
```

### TODO: write something about fusion of i18n on both server side and client side, and json/js parameters in i18nUtils.py

