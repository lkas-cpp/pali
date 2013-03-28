#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, json


translationInfo = {
  'zh_TW': {
    'canon': {
      's0201m.mul0.xml': ['3'],
      's0201m.mul1.xml': ['3'],
      's0201m.mul2.xml': ['3'],
      's0201m.mul3.xml': ['3'],
      's0201m.mul4.xml': ['3'],
      's0202m.mul0.xml': ['3'],
      's0202m.mul1.xml': ['3'],
      's0202m.mul4.xml': ['3'],
      's0402m2.mul6.xml': ['3'],
      's0502m.mul0.xml': ['2'],
      's0502m.mul1.xml': ['2'],
      's0502m.mul2.xml': ['2'],
      's0502m.mul3.xml': ['2'],
      's0502m.mul4.xml': ['2'],
      's0505m.mul0.xml': ['1']
    },
    'source': {
      '1': ['郭良鋆', 'http://blog.yam.com/benji/article/34665984'],
      '2': ['了參法師(葉均)', 'http://myweb.ncku.edu.tw/~lsn46/Tipitaka/Sutta/Khuddaka/Dhammapada/ven-l-z-all.htm'],
      '3': ['蕭式球', 'http://www.chilin.edu.hk/edu/report_section.asp?section_id=5']
    }
  },
  'en_US': {
    'canon': {
      's0502m.mul0.xml': ['1'],
      's0502m.mul1.xml': ['1'],
      's0502m.mul2.xml': ['1'],
      's0502m.mul3.xml': ['1'],
      's0502m.mul4.xml': ['1']
    },
    'source': {
      '1': ['Ṭhānissaro Bhikkhu', 'http://www.accesstoinsight.org/tipitaka/translators.html#than', 'http://www.accesstoinsight.org/lib/authors/thanissaro/dhammapada.pdf']
    }
  }
}

canonName = {
  's0201m.mul0.xml': {
    'pali': 'Mūlapariyāyavaggo, Mūlapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '根本法門品, 根本五十經, 中部, 經藏'
  },
  's0201m.mul1.xml': {
    'pali': 'Sīhanādavaggo, Mūlapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '獅子吼品, 根本五十經, 中部, 經藏'
  },
  's0201m.mul2.xml': {
    'pali': 'Opammavaggo, Mūlapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '譬喻品, 根本五十經, 中部, 經藏'
  },
  's0201m.mul3.xml': {
    'pali': 'Mahāyamakavaggo, Mūlapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '雙大品, 根本五十經, 中部, 經藏'
  },
  's0201m.mul4.xml': {
    'pali': 'Cūḷayamakavaggo, Mūlapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '雙小品, 根本五十經, 中部, 經藏'
  },
  's0202m.mul0.xml': {
    'pali': 'Gahapativaggo, Majjhimapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '居士品, 中分五十經篇, 中部, 經藏'
  },
  's0202m.mul1.xml': {
    'pali': 'Bhikkhuvaggo, Majjhimapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '比丘品, 中分五十經篇, 中部, 經藏'
  },
  's0202m.mul4.xml': {
    'pali': 'Brāhmaṇavaggo, Majjhimapaṇṇāsa, Majjhima, Sutta',
    'zh_TW': '婆羅門品, 中分五十經篇, 中部, 經藏'
  },
  's0402m2.mul6.xml': {
    'pali': 'Mahāvaggo, Tikanipāta, Aṅguttara, Sutta',
    'zh_TW': '大品, 三集, 增支部, 經藏'
  },
  's0505m.mul0.xml': {
    'pali': 'Uragavaggo, Suttanipāta, Khuddaka, Sutta',
    'zh_TW': '蛇品, 經集, 小部, 經藏'
  },
  's0502m.mul0.xml': {
    'pali': 'Dhammapada, Yamakavaggo',
    'en_US': 'Dhammapada, Pairs',
    'zh_TW': '法句, 雙品'
  },
  's0502m.mul1.xml': {
    'pali': 'Dhammapada, Appamādavaggo',
    'en_US': 'Dhammapada, Heedfulness',
    'zh_TW': '法句, 不放逸品'
  },
  's0502m.mul2.xml': {
    'pali': 'Dhammapada, Cittavaggo',
    'en_US': 'Dhammapada, The Mind',
    'zh_TW': '法句, 心品'
  },
  's0502m.mul3.xml': {
    'pali': 'Dhammapada, Pupphavaggo',
    'en_US': 'Dhammapada, Blossoms',
    'zh_TW': '法句, 華(花)品'
  },
  's0502m.mul4.xml': {
    'pali': 'Dhammapada, Bālavaggo',
    'en_US': 'Dhammapada, Fools',
    'zh_TW': '法句, 愚品'
  }
}


canonTextTranslation = {}
# http://www.accesstoinsight.org/tipitaka/index.html
# http://www.xin-yuan.com/cityzen/jiangtan/AHAN/ahan.htm
canonTextTranslation['en_US'] = {
#'Vinayapiṭaka': 'The Book of the Discipline',
  'Dīghanikāya': 'Long Discourses',
    'Sīlakkhandhavaggapāḷi':'The Division Concerning Morality',
      'Brahmajālasuttaṃ': 'The All-embracing Net of Views',
      'Sāmaññaphalasuttaṃ': 'The Fruits of the Contemplative Life',
    'Mahāvaggapāḷi':'The Large Division',
#     'Mahāpadānasuttaṃ': '',
      'Mahānidānasuttaṃ': 'The Great Causes Discourse',
#     'Mahāparinibbānasuttaṃ': '',
#     'Mahāsudassanasuttaṃ': '',
#     'Janavasabhasuttaṃ': '',
#     'Mahāgovindasuttaṃ': '',
      'Mahāsamayasuttaṃ': 'The Great Assembly/The Great Meeting',
      'Sakkapañhasuttaṃ': "Sakka's Questions",
      'Mahāsatipaṭṭhānasuttaṃ': 'The Great Frames of Reference',
#     'Pāyāsisuttaṃ': '',
    'Pāthikavaggapāḷi':'The Pāthika Division',
#     'Pāthikasuttaṃ': '',
#     'Udumbarikasuttaṃ': '',
      'Cakkavattisuttaṃ': 'The Wheel-turning Emperor',
#     'Aggaññasuttaṃ': '',
#     'Sampasādanīyasuttaṃ': '',
#     'Pāsādikasuttaṃ': '',
#     'Lakkhaṇasuttaṃ': '',
      'Siṅgālasuttaṃ': "The Buddha's Advice to Sigalaka/The Discourse to Sigala",
      'Āṭānāṭiyasuttaṃ': 'Discourse on Āṭānāṭiya',
#     'Saṅgītisuttaṃ': '',
#     'Dasuttarasuttaṃ': '',
  'Majjhimanikāya': 'Middle-length Discourses',
  'Saṃyuttanikāya': 'Grouped" Discourses',
  'Aṅguttaranikāya': 'Further-factored Discourses',
  'Khuddakanikāya': 'Division of Short Books',
#'Abhidhammapiṭaka': '',
  'Dhammasaṅgaṇīpāḷi': 'Enumeration of Phenomena',
  'Vibhaṅgapāḷi': 'The Book of Analysis',
  'Dhātukathāpāḷi': 'Discourse on Elements',
  'Puggalapaññattipāḷi': 'A Designation of Human Types',
  'Kathāvatthupāḷi': 'Points of Controversy',
# 'Yamakapāḷi': '',
# 'Paṭṭhānapāḷi': '',
' ': ' '
}

# http://www.therawikipedia.org/wiki/%E5%A2%9E%E6%94%AF%E9%83%A8
# http://yifertw.blogspot.tw/2008/04/9-2008421.html
canonTextTranslation['zh_TW'] = {
'Vinayapiṭaka': '律藏',
  'Pārājikapāḷi': '波羅夷品',
#   'Verañjakaṇḍaṃ': '',
    'Pārājikakaṇḍaṃ': '波羅夷 (他勝,斷頭)章',
    'Saṅghādisesakaṇḍaṃ': '僧殘 (僧伽胝施沙)章',
    'Aniyatakaṇḍaṃ': '不定章',
    'Nissaggiyakaṇḍaṃ': '捨墮 (尼薩耆波逸提)章',
  'Pācittiyapāḷi': '波逸提品',
    'Pācittiyakaṇḍaṃ': '波逸提 (單墮)章',
    'Pāṭidesanīyakaṇḍaṃ': '悔過 (波胝提舍尼)章',
    'Sekhiyakaṇḍaṃ': '眾學章',
    'Adhikaraṇasamathā': '滅諍',
    'bhikkhunīvibhaṅgo': '比丘尼分別',
  'Mahāvaggapāḷi': '大品',
    'Mahākhandhako': '大篇 (大犍度)',
    'Uposathakkhandhako': '伍波薩他篇 (布薩犍度)',
    'Vassūpanāyikakkhandhako': '入雨安居篇 (入雨安居犍度)',
    'Pavāraṇākkhandhako': '自恣篇 (自恣犍度)',
    'Cammakkhandhako': '皮革篇 (皮革犍度)',
    'Bhesajjakkhandhako': '藥篇 (藥犍度)',
    'Kathinakkhandhako': '咖提那篇 (迦絺那衣犍度)',
    'Cīvarakkhandhako': '衣篇 (衣犍度)',
    'Campeyyakkhandhako': '瞻巴篇 (瞻波犍度)',
    'Kosambakakkhandhako': '高賞比篇 (拘晱彌犍度)',
  'Cūḷavaggapāḷi': '小品',
    'Kammakkhandhakaṃ': '甘馬篇 (羯摩犍度)',
    'Pārivāsikakkhandhakaṃ': '別住篇 (別住犍度)',
    'Samuccayakkhandhakaṃ': '集篇 (集犍度)',
    'Samathakkhandhakaṃ': '止篇 (滅諍犍度)',
    'Khuddakavatthukkhandhakaṃ': '小事篇 (小犍度)',
    'Senāsanakkhandhakaṃ': '坐卧處篇 (臥坐具犍度)',
    'Saṅghabhedakakkhandhakaṃ': '破僧篇 (破僧犍度)',
    'Vattakkhandhakaṃ': '行儀篇 (儀法犍度)',
    'Pātimokkhaṭṭhapanakkhandhakaṃ': '遮誦戒篇 (遮說戒犍度)',
    'Bhikkhunikkhandhakaṃ': '比庫尼篇 (比丘尼犍度)',
    'Pañcasatikakkhandhakaṃ': '五百篇 (五百結集犍度)',
    'Sattasatikakkhandhakaṃ': '七百篇 (七百結集犍度)',
  'Parivārapāḷi': '附隨',
#   'Soḷasamahāvāro': '',
    'Samuṭṭhānasīsasaṅkhepo': '等起攝頌 (等起)',
    'Antarapeyyālaṃ': '無間省略',
    'Khandhakapucchāvāro': '問犍度章',
    'Ekuttarikanayo': '增一法',
    'Uposathādipucchāvissajjanā': '伍波薩他初解答章 (布薩初解答以及制戒義利論)',
    'Gāthāsaṅgaṇikaṃ': '伽陀集',
    'Adhikaraṇabhedo': '諍事分解',
    'Aparagāthāsaṅgaṇikaṃ': '別伽陀集',
    'Codanākaṇḍaṃ': '呵責品',
    'Cūḷasaṅgāmo': '小諍',
    'Mahāsaṅgāmo': '大諍',
    'Kathinabhedo': '咖提那衣分解 (迦絺那衣分解)',
    'Upālipañcakaṃ': '伍巴離五法 (優婆離五法)',
    'Atthāpattisamuṭṭhānaṃ': '等起',
    'Dutiyagāthāsaṅgaṇikaṃ': '第二伽陀集',
    'Sedamocanagāthā': '發汗偈',
    'Pañcavaggo': '五品',
'Suttapiṭaka': '經藏',
  'Dīghanikāya': '長部',
    'Sīlakkhandhavaggapāḷi':'戒蘊品',
      'Brahmajālasuttaṃ': '梵網經',
      'Sāmaññaphalasuttaṃ': '沙門果經',
      'Ambaṭṭhasuttaṃ': '阿摩晝經',
      'Soṇadaṇḍasuttaṃ': '種德經',
      'Kūṭadantasuttaṃ': '究羅檀頭經',
      'Mahālisuttaṃ': '摩訶梨經',
      'Jāliyasuttaṃ': '闍利經',
      'Mahāsīhanādasuttaṃ': '迦葉獅子吼經',
      'Poṭṭhapādasuttaṃ': '布吒婆樓經',
      'Subhasuttaṃ': '須婆經',
      'Kevaṭṭasuttaṃ': '堅固經',
      'Lohiccasuttaṃ': '露遮經',
      'Tevijjasuttaṃ': '三明經',
    'Mahāvaggapāḷi':'大品',
      'Mahāpadānasuttaṃ': '大本經',
      'Mahānidānasuttaṃ': '大緣經',
      'Mahāparinibbānasuttaṃ': '大般涅槃經',
      'Mahāsudassanasuttaṃ': '大善見王經',
      'Janavasabhasuttaṃ': '闍尼沙經',
      'Mahāgovindasuttaṃ': '大典尊經',
      'Mahāsamayasuttaṃ': '大會經',
      'Sakkapañhasuttaṃ': '帝釋所問經',
      'Mahāsatipaṭṭhānasuttaṃ': '大念處經',
      'Pāyāsisuttaṃ': '弊宿經',
    'Pāthikavaggapāḷi':'波梨品',
      'Pāthikasuttaṃ': '波梨經',
      'Udumbarikasuttaṃ': '優曇婆邏獅子吼經',
      'Cakkavattisuttaṃ': '轉輪聖王獅子吼經',
      'Aggaññasuttaṃ': '起世因本經',
      'Sampasādanīyasuttaṃ': '自歡喜經',
      'Pāsādikasuttaṃ': '清淨經',
      'Lakkhaṇasuttaṃ': '三十二相經',
      'Siṅgālasuttaṃ': '教授屍迦羅越經',
      'Āṭānāṭiyasuttaṃ': '阿吒曩胝經',
      'Saṅgītisuttaṃ': '等誦經',
      'Dasuttarasuttaṃ': '十上經',
  'Majjhimanikāya': '中部',
    'Mūlapaṇṇāsapāḷi': '根本五十經編',
      'Mūlapariyāyavaggo': '根本法門品',
      'Sīhanādavaggo': '師子吼品',
      'Opammavaggo': '譬喻品',
      'Mahāyamakavaggo': '大雙品',
      'Cūḷayamakavaggo': '小雙品',
    'Majjhimapaṇṇāsapāḷi': '中分五十經編',
      'Gahapativaggo': '居士品',
      'Bhikkhuvaggo': '比丘品',
      'Paribbājakavaggo': '遊行者品',
      'Rājavaggo': '王品',
      'Brāhmaṇavaggo': '婆羅門品',
    'Uparipaṇṇāsapāḷi': '後分五十經編',
      'Devadahavaggo': '天臂品',
      'Anupadavaggo': '緊隨品',
      'Suññatavaggo': '空品',
      'Vibhaṅgavaggo': '分別品',
      'Saḷāyatanavaggo': '六處品',
  'Saṃyuttanikāya': '相應部',
    'Sagāthāvaggapāḷi': '有偈篇',
      'Devatāsaṃyuttaṃ': '諸天相應',
      'Devaputtasaṃyuttaṃ': '天子相應',
      'Kosalasaṃyuttaṃ': '憍薩羅相應',
      'Mārasaṃyuttaṃ': '魔羅相應',
      'Bhikkhunīsaṃyuttaṃ': '比丘尼相應',
      'Brahmasaṃyuttaṃ': '梵天相應',
      'Brāhmaṇasaṃyuttaṃ': '婆羅門相應',
      'Vaṅgīsasaṃyuttaṃ': '婆耆沙長老相應',
      'Vanasaṃyuttaṃ': '森林相應',
      'Yakkhasaṃyuttaṃ': '夜叉相應',
      'Sakkasaṃyuttaṃ': '帝釋天帝相應',
    'Nidānavaggapāḷi': '因緣篇',
      'Nidānasaṃyuttaṃ': '因緣相應',
      'Abhisamayasaṃyuttaṃ': '現觀相應',
      'Dhātusaṃyuttaṃ': '界相應',
      'Anamataggasaṃyuttaṃ': '無始相應',
      'Kassapasaṃyuttaṃ': '迦葉相應',
      'Lābhasakkārasaṃyuttaṃ': '利得與供養相應',
      'Rāhulasaṃyuttaṃ': '羅睺羅相應',
      'Lakkhaṇasaṃyuttaṃ': '勒叉那相應',
      'Opammasaṃyuttaṃ': '譬喻相應',
      'Bhikkhusaṃyuttaṃ': '比丘相應',
    'Khandhavaggapāḷi': '蘊篇',
      'Khandhasaṃyuttaṃ': '蘊相應',
      'Rādhasaṃyuttaṃ': '羅陀相應',
      'Diṭṭhisaṃyuttaṃ': '見相應',
      'Okkantasaṃyuttaṃ': '入相應',
      'Uppādasaṃyuttaṃ': '生相應',
      'Kilesasaṃyuttaṃ': '煩惱相應',
      'Sāriputtasaṃyuttaṃ': '舍利弗相應',
      'Nāgasaṃyuttaṃ': '龍相應',
      'Supaṇṇasaṃyuttaṃ': '金翅鳥相應',
      'Gandhabbakāyasaṃyuttaṃ': '乾闥婆相應',
      'Valāhakasaṃyuttaṃ': '雲相應',
      'Vacchagottasaṃyuttaṃ': '婆磋種相應',
      'Jhānasaṃyuttaṃ': '禪定相應',
    'Saḷāyatanavaggapāḷi': '六處篇',
      'Saḷāyatanasaṃyuttaṃ': '六處相應',
      'Vedanāsaṃyuttaṃ': '受相應',
      'Mātugāmasaṃyuttaṃ': '女人相應',
      'Jambukhādakasaṃyuttaṃ': '閻浮車相應',
      'Sāmaṇḍakasaṃyuttaṃ': '沙門出家相應',
      'Moggallānasaṃyuttaṃ': '目犍連相應',
      'Cittasaṃyuttaṃ': '質多相應',
      'Gāmaṇisaṃyuttaṃ': '聚落主相應',
      'Asaṅkhatasaṃyuttaṃ': '無為相應',
      'Abyākatasaṃyuttaṃ': '無記相應',
#   'Mahāvaggapāḷi': '大篇',
      'Maggasaṃyuttaṃ': '道相應',
      'Bojjhaṅgasaṃyuttaṃ': '覺支相應',
      'Satipaṭṭhānasaṃyuttaṃ': '念處相應',
      'Indriyasaṃyuttaṃ': '根相應',
      'Sammappadhānasaṃyuttaṃ': '正勤相應',
      'Balasaṃyuttaṃ': '力相應',
      'Iddhipādasaṃyuttaṃ': '神足相應',
      'Anuruddhasaṃyuttaṃ': '阿那律相應',
#     'Jhānasaṃyuttaṃ': '靜慮相應',
      'Ānāpānasaṃyuttaṃ': '入出息相應',
      'Sotāpattisaṃyuttaṃ': '入流 (須陀洹)相應',
      'Saccasaṃyuttaṃ': '諦相應',
  'Aṅguttaranikāya': '增支部',
    'Ekakanipātapāḷi': '一集',
      'Rūpādivaggo': '色等品',
      'Nīvaraṇappahānavaggo': '斷蓋品',
      'Akammaniyavaggo': '無堪忍品',
      'Adantavaggo': '無調品',
      'Paṇihitaacchavaggo': '向與隱覆品',
      'Accharāsaṅghātavaggo': '彈指品',
      'Vīriyārambhādivaggo': '發精進等品',
      'Kalyāṇamittādivaggo': '善友等品',
      'Pamādādivaggo': '放逸等品',
#     'Dutiyapamādādivaggo': '',
      'Adhammavaggo': '非法等品',
      'Anāpattivaggo': '無范等品',
      'Ekapuggalavaggo': '一人品',
      'Etadaggavaggo': '是第一品',
      'Aṭṭhānapāḷi': '無有是處品',
      'Ekadhammapāḷi': '一法品',
      'Pasādakaradhammavaggo': '種子品',
      'Aparaaccharāsaṅghātavaggo': '末伽梨品',
      'Kāyagatāsativaggo': '不放逸品',
      'Amatavaggo': '靜慮品',
    'Dukanipātapāḷi': '二集',
      'Kammakaraṇavaggo': '科刑罰品',
      'Adhikaraṇavaggo': '靜論品',
      'Bālavaggo': '愚人品',
      'Samacittavaggo': '等心品',
      'Parisavaggo': '會眾品',
      'Puggalavaggo': '人品',
      'Sukhavaggo': '樂品',
      'Sanimittavaggo': '有品',
      'Dhammavaggo': '法品',
#     'Bālavaggo': '愚者品',
      'Āsāduppajahavaggo': '希望品',
      'Āyācanavaggo': '希求品',
      'Dānavaggo': '施品',
      'Santhāravaggo': '覆護品',
      'Samāpattivaggo': '入定品',
      'Kodhapeyyālaṃ': '忿品',
      'Akusalapeyyālaṃ': '(律廣說)品',
#     'Vinayapeyyālaṃ': '',
#     'Rāgapeyyālaṃ': '',
    'Tikanipātapāḷi': '三集',
#     'Bālavaggo': '愚人品',
      'Rathakāravaggo': '車匠品',
#     'Puggalavaggo': '補特羅品',
      'Devadūtavaggo': '天使品',
#     'Cūḷavaggo': '小品',
#     'Brāhmaṇavaggo': '婆羅門品',
#     'Mahāvaggo': '大品',
      'Ānandavaggo': '阿難品',
      'Samaṇavaggo': '沙門品',
      'Loṇakapallavaggo': '掬鹽品',
      'Sambodhavaggo': '等覺品',
      'Āpāyikavaggo': '惡趣品',
      'Kusināravaggo': '古西那拉品',
      'Yodhājīvavaggo': '戰士品',
      'Maṅgalavaggo': '吉祥品',
      'Acelakavaggo': '裸形品',
#     'Kammapathapeyyālaṃ': '',
#     'Rāgapeyyālaṃ': '',
    'Catukkanipātapāḷi': '四集',
    'Pañcakanipātapāḷi': '五集',
    'Chakkanipātapāḷi': '六集',
    'Sattakanipātapāḷi': '七集',
    'Aṭṭhakādinipātapāḷi': '八集',
    'Navakanipātapāḷi': '九集',
    'Dasakanipātapāḷi': '十集',
    'Ekādasakanipātapāḷi': '十一集',
      'Nissayavaggo': '依止品',
      'Anussativaggo': '憶念品',
      'Sāmaññavaggo': '沙門品',
      'Rāgapeyyālaṃ': '貪品',
  'Khuddakanikāya': '小部',
    'Khuddakapāṭhapāḷi': '小誦',
    'Dhammapadapāḷi': '法句',
    'Udānapāḷi': '自說',
    'Itivuttakapāḷi': '如是語',
    'Suttanipātapāḷi': '經集',
      'Uragavaggo': '蛇品',
      'Cūḷavaggo': '小品',
      'Mahāvaggo': '大品',
      'Aṭṭhakavaggo': '八頌經品',
      'Pārāyanavaggo': '彼岸道品',
    'Vimānavatthupāḷi': '天宮事',
    'Petavatthupāḷi': '餓鬼事',
    'Theragāthāpāḷi': '長老偈',
    'Therīgāthāpāḷi': '長老尼偈',
    'Apadānapāḷi': '譬喻',
    'Buddhavaṃsapāḷi': '佛種姓 (諸佛史)',
    'Cariyāpiṭakapāḷi': '所行藏',
    'Jātakapāḷi': '本生',
    'Mahāniddesapāḷi': '大義釋',
    'Cūḷaniddesapāḷi': '小義釋',
    'Paṭisambhidāmaggapāḷi': '無礙解道',
    'Nettippakaraṇapāḷi': '導論',
    'Milindapañhapāḷi': '彌林達問經 (彌林達王問經,那先比丘經)',
    'Peṭakopadesapāḷi': '藏釋 (三藏知津)',
'Abhidhammapiṭaka': '論藏 (阿毘達摩)',
  'Dhammasaṅgaṇīpāḷi': '法集論',
  'Vibhaṅgapāḷi': '分別論',
  'Dhātukathāpāḷi': '界說論',
  'Puggalapaññattipāḷi': '人施設論',
  'Kathāvatthupāḷi': '論事',
  'Yamakapāḷi': '雙對論',
  'Paṭṭhānapāḷi': '發趣論',
' ': ' '
}


if __name__ == '__main__':
  dstTrInfoPath = os.path.join(os.path.dirname(__file__), 'json/translationInfo.json')
  dstCanonNamePath = os.path.join(os.path.dirname(__file__), 'json/canonName.json')
  dstCanonTextTranslationPath = os.path.join(os.path.dirname(__file__), 'json/canonTextTranslation.json')

  if not os.path.exists(os.path.dirname(dstTrInfoPath)):
    os.makedirs(os.path.dirname(dstTrInfoPath))

  with open(dstTrInfoPath, 'w') as f:
    f.write(json.dumps(translationInfo))

  with open(dstCanonNamePath, 'w') as f:
    f.write(json.dumps(canonName))

  with open(dstCanonTextTranslationPath, 'w') as f:
    f.write(json.dumps(canonTextTranslation))

  dstTrServicePath = os.path.join(os.path.dirname(__file__), '../app/js/data-i18nTpk-service.js')

  with open(dstTrServicePath, 'w') as f:
    f.write("angular.module('pali.data.i18nTpk', []).\n")
    f.write("  factory('i18nTpk', [function() {\n")
    f.write("    var translationInfo = ")
    f.write(json.dumps(translationInfo))
    f.write(";\n")
    f.write("    var canonName = ")
    f.write(json.dumps(canonName))
    f.write(";\n")
    f.write("    var canonTextTranslation = ")
    f.write(json.dumps(canonTextTranslation))
    f.write(";\n")
    f.write("    var serviceInstance = { translationInfo: translationInfo, canonName: canonName, canonTextTranslation: canonTextTranslation };\n")
    f.write("    return serviceInstance;\n")
    f.write("  }]);\n")
