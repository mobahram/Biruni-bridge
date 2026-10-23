"""Center-profile copy that was still English on the directory pages."""

from __future__ import annotations

A = "\u2019"
D = "\u2013"

CENTER_ROWS: list[tuple[str, str, str, str, str, str]] = []


def add(en, ru, es, fr, ur, fa):
    CENTER_ROWS.append((en, ru, es, fr, ur, fa))


def same(en):
    add(en, en, en, en, en, en)


add(
    "ENT (Otorhinolaryngology)",
    "ЛОР (оториноларингология)",
    "ORL (otorrinolaringología)",
    "ORL (oto-rhino-laryngologie)",
    "ناک کان گلا (اوٹولیرینگولوجی)",
    "گوش و حلق و بینی (اتولارینگولوژی)",
)
add(
    "Interventional radiology",
    "Интервенционная радиология",
    "Radiología intervencionista",
    "Radiologie interventionnelle",
    "مداخلاتی ریڈیولوجی",
    "رادیولوژی مداخله‌ای",
)

# Bone marrow transplant center
add(
    "A dated list of previous treatments and the current disease status (for example, remission)",
    "Датированный список предыдущего лечения и текущий статус болезни (например, ремиссия)",
    "Una lista fechada de tratamientos previos y el estado actual de la enfermedad (por ejemplo, remisión)",
    "Une liste datée des traitements antérieurs et l’état actuel de la maladie (par exemple, une rémission)",
    "سابقہ علاج کی تاریخ کے ساتھ فہرست اور بیماری کی موجودہ حالت (مثلاً معافی)",
    "فهرست تاریخ‌دار درمان‌های قبلی و وضعیت فعلی بیماری (برای مثال، بهبودی)",
)
add(
    "A detailed report for your doctor, and long-term follow-up coordinated with the team in Istanbul.",
    "Подробное заключение для вашего врача и длительное наблюдение вместе с командой в Стамбуле.",
    "Un informe detallado para su médico y un seguimiento a largo plazo coordinado con el equipo de Estambul.",
    "Un compte rendu détaillé pour votre médecin, et un suivi à long terme coordonné avec l’équipe d’Istanbul.",
    "آپ کے ڈاکٹر کے لیے تفصیلی رپورٹ، اور استنبول کی ٹیم کے ساتھ طویل فالو اپ۔",
    "گزارش دقیق برای پزشک شما، و پیگیری بلندمدت هماهنگ با تیم استانبول.",
)
add(
    "A transplant is one option among several. Whether it suits you depends on the disease and its stage, how you responded to previous treatment, your general health and, for an allogeneic transplant, a suitable donor. The treating physician decides.",
    "Трансплантация — один из вариантов. Подходит ли она, зависит от болезни и её стадии, ответа на предыдущее лечение, общего состояния и, при аллогенной трансплантации, от подходящего донора. Решает лечащий врач.",
    "El trasplante es una opción entre varias. Si le conviene depende de la enfermedad y su estadio, de la respuesta al tratamiento previo, de su salud general y, en un trasplante alogénico, de un donante adecuado. Decide el médico tratante.",
    "La greffe est une option parmi d’autres. Qu’elle vous convienne dépend de la maladie et de son stade, de la réponse aux traitements antérieurs, de votre état général et, pour une allogreffe, d’un donneur adapté. Le médecin traitant décide.",
    "ٹرانسپلانٹ کئی اختیارات میں سے ایک ہے۔ یہ آپ کے لیے موزوں ہے یا نہیں، بیماری اور اس کے مرحلے، پچھلے علاج کے جواب، عمومی صحت اور ایلو جینک ٹرانسپلانٹ کے لیے موزوں عطیہ دہندہ پر منحصر ہے۔ فیصلہ معالج کرتا ہے۔",
    "پیوند یکی از چند گزینه است. مناسب بودن آن به بیماری و مرحلهٔ آن، پاسخ به درمان قبلی، سلامت عمومی و، برای پیوند آلوژن، به دهندهٔ مناسب بستگی دارد. پزشک معالج تصمیم می‌گیرد.",
)
add(
    "Acute & chronic leukemias (AML, ALL, CML, CLL)",
    "Острые и хронические лейкозы (AML, ALL, CML, CLL)",
    "Leucemias agudas y crónicas (AML, ALL, CML, CLL)",
    "Leucémies aiguës et chroniques (AML, ALL, CML, CLL)",
    "شدید اور دائمی لیوکیمیا (AML, ALL, CML, CLL)",
    "لوسمی حاد و مزمن (AML, ALL, CML, CLL)",
)
add("Adults & children", "Взрослые и дети", "Adultos y niños", "Adultes et enfants", "بالغ اور بچے", "بزرگسال و کودک")
add(
    "Allogeneic, matched relative",
    "Аллогенная, совместимый родственник",
    "Alogénico, familiar compatible",
    "Allogénique, parent compatible",
    "ایلو جینک، مماثل رشتہ دار",
    "آلوژن، خویشاوند سازگار",
)
add(
    "Allogeneic, unrelated donor",
    "Аллогенная, неродственный донор",
    "Alogénico, donante no emparentado",
    "Allogénique, donneur non apparenté",
    "ایلو جینک، غیر متعلق عطیہ دہندہ",
    "آلوژن، دهندهٔ غیرخویشاوند",
)
add("Aplastic anemia", "Апластическая анемия", "Anemia aplásica", "Aplasie médullaire", "اپلاسٹک انیمیا", "کم‌خونی آپلاستیک")
add("Auto & allo", "Ауто и алло", "Auto y alo", "Auto et allo", "آٹو اور ایلو", "اتولوگ و آلوژن")
add("Autologous", "Аутологичная", "Autólogo", "Autologue", "آٹولوگس", "اتولوگ")
add("Blood cancers", "Рак крови", "Cánceres de la sangre", "Cancers du sang", "خون کے کینسر", "سرطان‌های خون")
add(
    "Bone marrow biopsy and aspirate results, including flow cytometry or genetic tests if done",
    "Результаты биопсии и аспирата костного мозга, включая проточную цитометрию или генетические тесты, если они сделаны",
    "Resultados de biopsia y aspirado de médula ósea, incluida la citometría de flujo o pruebas genéticas si se hicieron",
    "Résultats de biopsie et d’aspiration de moelle osseuse, y compris la cytométrie en flux ou les tests génétiques s’ils ont été faits",
    "بون میرو بایوپسی اور اسپیریٹ کے نتائج، بشمول فلو سائٹومیٹری یا جینیاتی ٹیسٹ اگر ہو چکے ہوں",
    "نتایج بیوپسی و آسپیراسیون مغز استخوان، از جمله فلوسیتومتری یا آزمایش ژنتیک اگر انجام شده باشد",
)
add("Bone marrow disorders", "Болезни костного мозга", "Trastornos de la médula ósea", "Atteintes de la moelle osseuse", "بون میرو کے عوارض", "اختلال‌های مغز استخوان")
add(
    "Brothers and sisters are usually tested first with an HLA tissue-typing test. We send you the list of required tests; if no matched sibling is found, the team explains the other options for your case.",
    "Сначала обычно типируют братьев и сестёр по HLA. Мы присылаем список нужных анализов; если совместимого брата или сестры нет, команда объясняет другие варианты для вашего случая.",
    "Por lo general primero se tipan los hermanos con una prueba HLA. Le enviamos la lista de pruebas necesarias; si no hay un hermano compatible, el equipo explica las otras opciones de su caso.",
    "Les frères et sœurs sont en général typés en premier par un test HLA. Nous vous envoyons la liste des examens requis ; si aucun frère ou sœur compatible n’est trouvé, l’équipe explique les autres options pour votre cas.",
    "عام طور پر پہلے بھائی بہنوں کا HLA ٹشو ٹائپنگ ٹیسٹ ہوتا ہے۔ ہم مطلوبہ ٹیسٹوں کی فہرست بھیجتے ہیں؛ اگر مماثل بہن بھائی نہ ملے تو ٹیم آپ کے کیس کے دوسرے اختیارات بتاتی ہے۔",
    "معمولاً ابتدا خواهر و برادر با آزمایش HLA نوع‌بافت بررسی می‌شوند. فهرست آزمایش‌های لازم را می‌فرستیم؛ اگر خواهر یا برادر سازگار پیدا نشود، تیم گزینه‌های دیگر پروندهٔ شما را توضیح می‌دهد.",
)
add("CAR-T cell therapy", "Клеточная терапия CAR-T", "Terapia celular CAR-T", "Thérapie cellulaire CAR-T", "CAR-T سیل تھراپی", "درمان سلولی CAR-T")
add(
    "Can my brother or sister be the donor?",
    "Может ли брат или сестра быть донором?",
    "¿Puede ser donante mi hermano o mi hermana?",
    "Mon frère ou ma sœur peut-il être le donneur ?",
    "کیا میرا بھائی یا بہن عطیہ دہندہ بن سکتا/سکتی ہے؟",
    "آیا برادر یا خواهرم می‌تواند دهنده باشد؟",
)
add("Cell collection", "Сбор клеток", "Recogida de células", "Recueil des cellules", "خلیوں کا جمع کرنا", "جمع‌آوری سلول")
add(
    "Chemotherapy, sometimes with radiotherapy, to prepare the bone marrow.",
    "Химиотерапия, иногда с лучевой терапией, чтобы подготовить костный мозг.",
    "Quimioterapia, a veces con radioterapia, para preparar la médula ósea.",
    "Chimiothérapie, parfois avec radiothérapie, pour préparer la moelle osseuse.",
    "کیمیوتھراپی، کبھی ریڈیوتھراپی کے ساتھ، بون میرو کو تیار کرنے کے لیے۔",
    "شیمی‌درمانی، گاهی همراه پرتودرمانی، برای آماده کردن مغز استخوان.",
)
add("Conditioning", "Кондиционирование", "Acondicionamiento", "Conditionnement", "کنڈیشننگ", "آماده‌سازی")
add("Diagnosis and pathology reports", "Диагноз и патоморфологические заключения", "Informes de diagnóstico y anatomía patológica", "Comptes rendus de diagnostic et d’anatomopathologie", "تشخیص اور پیتھالوجی رپورٹس", "گزارش تشخیص و آسیب‌شناسی")
add(
    "Diagnosis and pathology reports, bone marrow biopsy results, recent blood tests, a dated list of previous treatments and the current disease status, and HLA typing results for you and your siblings if already done.",
    "Диагноз и патоморфологические заключения, результаты биопсии костного мозга, недавние анализы крови, датированный список предыдущего лечения и текущий статус болезни, а также результаты HLA-типирования вас и братьев и сестёр, если они уже есть.",
    "Informes de diagnóstico y anatomía patológica, resultados de biopsia de médula, análisis de sangre recientes, una lista fechada de tratamientos previos y el estado actual de la enfermedad, y los resultados de tipaje HLA suyos y de sus hermanos si ya se hicieron.",
    "Comptes rendus de diagnostic et d’anatomopathologie, résultats de biopsie de moelle, analyses de sang récentes, une liste datée des traitements antérieurs et l’état actuel de la maladie, et les résultats de typage HLA pour vous et vos frères et sœurs s’ils existent déjà.",
    "تشخیص اور پیتھالوجی رپورٹس، بون میرو بایوپسی کے نتائج، حالیہ خون کے ٹیسٹ، سابقہ علاج کی تاریخ والی فہرست اور بیماری کی موجودہ حالت، اور اگر ہو چکے ہوں تو آپ اور بہن بھائیوں کے HLA ٹائپنگ نتائج۔",
    "گزارش تشخیص و آسیب‌شناسی، نتایج بیوپسی مغز استخوان، آزمایش خون اخیر، فهرست تاریخ‌دار درمان‌های قبلی و وضعیت فعلی بیماری، و اگر انجام شده باشد نتایج HLA شما و خواهر و برادرها.",
)
add(
    "Discharge and stay near the hospital",
    "Выписка и пребывание рядом с больницей",
    "Alta y estancia cerca del hospital",
    "Sortie et séjour près de l’hôpital",
    "ڈسچارج اور ہسپتال کے قریب قیام",
    "ترخیص و اقامت نزدیک بیمارستان",
)
add(
    "Do you perform bone marrow transplants for adults and children?",
    "Делаете ли вы трансплантацию костного мозга взрослым и детям?",
    "¿Realizan trasplantes de médula ósea en adultos y niños?",
    "Faites-vous des greffes de moelle osseuse chez l’adulte et l’enfant ?",
    "کیا آپ بالغوں اور بچوں کا بون میرو ٹرانسپلانٹ کرتے ہیں؟",
    "آیا پیوند مغز استخوان برای بزرگسال و کودک انجام می‌دهید؟",
)
add(
    "Documents to send for a transplant review",
    "Документы для разбора перед трансплантацией",
    "Documentos para una revisión de trasplante",
    "Documents à envoyer pour un examen de greffe",
    "ٹرانسپلانٹ جائزے کے لیے بھیجنے والی دستاویزات",
    "مدارک برای بررسی پیوند",
)
add(
    "Does the donor need to travel with me?",
    "Нужно ли донору ехать вместе со мной?",
    "¿El donante tiene que viajar conmigo?",
    "Le donneur doit-il voyager avec moi ?",
    "کیا عطیہ دہندہ کو میرے ساتھ سفر کرنا ہوگا؟",
    "آیا دهنده باید با من سفر کند؟",
)
add("Donor testing, if needed", "Обследование донора, если нужно", "Pruebas del donante, si hacen falta", "Examens du donneur, si besoin", "اگر ضرورت ہو تو عطیہ دہندہ کے ٹیسٹ", "آزمایش دهنده، اگر لازم باشد")
add(
    f"For an allogeneic transplant, brothers and sisters are usually tested first with an HLA tissue-typing test. A related donor travels to Istanbul for medical tests and cell collection, and their own safety is assessed separately. We send you the list of required tests and help arrange the donor{A}s stay.",
    "При аллогенной трансплантации сначала обычно типируют братьев и сестёр по HLA. Родственный донор приезжает в Стамбул на обследования и сбор клеток, а его собственную безопасность оценивают отдельно. Мы присылаем список нужных анализов и помогаем организовать пребывание донора.",
    "En un trasplante alogénico, por lo general primero se tipan los hermanos con una prueba HLA. Un donante emparentado viaja a Estambul para las pruebas médicas y la recogida de células, y su propia seguridad se valora por separado. Le enviamos la lista de pruebas necesarias y ayudamos a organizar la estancia del donante.",
    "Pour une allogreffe, les frères et sœurs sont en général typés en premier par un test HLA. Un donneur apparenté se rend à Istanbul pour les examens et le recueil des cellules, et sa propre sécurité est évaluée séparément. Nous vous envoyons la liste des examens requis et aidons à organiser le séjour du donneur.",
    "ایلو جینک ٹرانسپلانٹ کے لیے عام طور پر پہلے بھائی بہنوں کا HLA ٹشو ٹائپنگ ٹیسٹ ہوتا ہے۔ رشتہ دار عطیہ دہندہ طبی ٹیسٹوں اور خلیے جمع کرنے کے لیے استنبول آتا ہے، اور اس کی اپنی حفاظت الگ سے دیکھی جاتی ہے۔ ہم مطلوبہ ٹیسٹوں کی فہرست بھیجتے ہیں اور عطیہ دہندہ کے قیام کا بندوبست کرنے میں مدد کرتے ہیں۔",
    "برای پیوند آلوژن، معمولاً ابتدا خواهر و برادر با آزمایش HLA نوع‌بافت بررسی می‌شوند. دهندهٔ خویشاوند برای آزمایش پزشکی و جمع‌آوری سلول به استانبول می‌آید و ایمنی خودش جداگانه ارزیابی می‌شود. فهرست آزمایش‌های لازم را می‌فرستیم و برای اقامت دهنده کمک می‌کنیم.",
)
add(
    "Frequent check-ups in the following weeks; allogeneic transplants usually need a longer stay.",
    "Частые осмотры в следующие недели; аллогенная трансплантация обычно требует более долгого пребывания.",
    "Controles frecuentes en las semanas siguientes; los trasplantes alogénicos suelen necesitar una estancia más larga.",
    "Des contrôles fréquents les semaines suivantes ; les allogreffes demandent en général un séjour plus long.",
    "اگلے ہفتوں میں بار بار چیک اپ؛ ایلو جینک ٹرانسپلانٹ کو عام طور پر لمبا قیام چاہیے۔",
    "ویزیت‌های مکرر در هفته‌های بعد؛ پیوند آلوژن معمولاً اقامت طولانی‌تری می‌خواهد.",
)
add("From a half-matched relative", "От наполовину совместимого родственника", "De un familiar semicompatible", "D’un parent semi-compatible", "آدھے مماثل رشتہ دار سے", "از خویشاوند نیم‌سازگار")
add(
    "From an HLA-matched brother or sister.",
    "От HLA-совместимого брата или сестры.",
    "De un hermano o hermana compatible por HLA.",
    "D’un frère ou d’une sœur compatible en HLA.",
    "HLA سے مماثل بھائی یا بہن سے۔",
    "از برادر یا خواهر سازگار HLA.",
)
add(
    "From the blood or bone marrow of the patient (autologous) or of the donor (allogeneic).",
    "Из крови или костного мозга пациента (аутологичная) или донора (аллогенная).",
    "De la sangre o la médula del paciente (autólogo) o del donante (alogénico).",
    "Du sang ou de la moelle du patient (autologue) ou du donneur (allogénique).",
    "مریض کے خون یا بون میرو سے (آٹولوگس) یا عطیہ دہندہ سے (ایلو جینک)۔",
    "از خون یا مغز استخوان بیمار (اتولوگ) یا دهنده (آلوژن).",
)
add("Full doctors directory", "Полный справочник врачей", "Directorio completo de médicos", "Annuaire complet des médecins", "ڈاکٹروں کی مکمل فہرست", "فهرست کامل پزشکان")
add(
    "HLA typing for brothers and sisters; the team tells you where and how it can be done.",
    "HLA-типирование братьев и сестёр; команда скажет, где и как его сделать.",
    "Tipaje HLA de hermanos; el equipo le dice dónde y cómo puede hacerse.",
    "Typage HLA des frères et sœurs ; l’équipe vous dit où et comment le faire.",
    "بھائی بہنوں کی HLA ٹائپنگ؛ ٹیم بتاتی ہے کہ یہ کہاں اور کیسے ہو سکتی ہے۔",
    "نوع‌بافت HLA خواهر و برادر؛ تیم می‌گوید کجا و چگونه انجام شود.",
)
add(
    "HLA typing results for you and your brothers or sisters, if already done",
    "Результаты HLA-типирования вас и братьев или сестёр, если уже сделаны",
    "Resultados de tipaje HLA suyos y de sus hermanos, si ya se hicieron",
    "Résultats de typage HLA pour vous et vos frères ou sœurs, s’ils existent déjà",
    "اگر ہو چکے ہوں تو آپ اور بھائی بہنوں کے HLA ٹائپنگ نتائج",
    "نتایج نوع‌بافت HLA شما و برادر یا خواهر، اگر انجام شده باشد",
)
add("Haploidentical", "Гаплоидентичная", "Haploidéntico", "Haplo-identique", "ہاپلو آئیڈینٹیکل", "هاپلوایدنتیکال")
add(
    "Heart, lung, infection and other tests to confirm the transplant is safe.",
    "Обследования сердца, лёгких, инфекций и другие тесты, чтобы подтвердить, что трансплантация безопасна.",
    "Pruebas de corazón, pulmón, infección y otras para confirmar que el trasplante es seguro.",
    "Examens du cœur, des poumons, des infections et d’autres tests pour confirmer que la greffe est sûre.",
    "دل، پھیپھڑے، انفیکشن اور دوسرے ٹیسٹ تاکہ تصدیق ہو کہ ٹرانسپلانٹ محفوظ ہے۔",
    "آزمایش قلب، ریه، عفونت و آزمایش‌های دیگر تا تأیید شود پیوند ایمن است.",
)
add(
    "Hemoglobinopathies (e.g. thalassemia)",
    "Гемоглобинопатии (например, талассемия)",
    "Hemoglobinopatías (p. ej. talasemia)",
    "Hémoglobinopathies (p. ex. thalassémie)",
    "ہیموگلوبینوپیتھیز (مثلاً تھیلیسیمیا)",
    "هموگلوبینوپاتی‌ها (مثلاً تالاسمی)",
)
add(
    "How long will I stay in Istanbul?",
    "Как долго я пробуду в Стамбуле?",
    "¿Cuánto tiempo estaré en Estambul?",
    "Combien de temps resterai-je à Istanbul ?",
    "میں استنبول میں کتنی دیر رہوں گا/گی؟",
    "چه مدت در استانبول می‌مانم؟",
)
add(
    "How much does a bone marrow transplant cost?",
    "Сколько стоит трансплантация костного мозга?",
    "¿Cuánto cuesta un trasplante de médula ósea?",
    "Combien coûte une greffe de moelle osseuse ?",
    "بون میرو ٹرانسپلانٹ کی لاگت کتنی ہے؟",
    "هزینهٔ پیوند مغز استخوان چقدر است؟",
)
add("If a donor is needed", "Если нужен донор", "Si hace falta un donante", "Si un donneur est nécessaire", "اگر عطیہ دہندہ درکار ہو", "اگر دهنده لازم باشد")
add("Immunity", "Иммунитет", "Inmunidad", "Immunité", "قوتِ مدافعت", "ایمنی")
add(
    f"In an autologous transplant, the patient{A}s own stem cells are collected and stored, then returned after high-dose treatment. In an allogeneic transplant, the cells come from a donor, often a matched brother or sister. The physicians choose the type according to the disease and its stage.",
    "При аутологичной трансплантации собственные стволовые клетки пациента собирают, сохраняют и возвращают после высокодозного лечения. При аллогенной клетки приходят от донора, часто от совместимого брата или сестры. Тип выбирают врачи по болезни и её стадии.",
    "En un trasplante autólogo se recogen y guardan las células madre del propio paciente y se devuelven tras un tratamiento a dosis altas. En un trasplante alogénico las células vienen de un donante, a menudo un hermano compatible. Los médicos eligen el tipo según la enfermedad y su estadio.",
    "Dans une autogreffe, les cellules souches du patient sont recueillies et conservées, puis rendues après un traitement à forte dose. Dans une allogreffe, les cellules viennent d’un donneur, souvent un frère ou une sœur compatible. Les médecins choisissent le type selon la maladie et son stade.",
    "آٹولوگس ٹرانسپلانٹ میں مریض کے اپنے اسٹیم سیل جمع کر کے محفوظ کیے جاتے ہیں، پھر زیادہ خوراک والے علاج کے بعد واپس دیے جاتے ہیں۔ ایلو جینک ٹرانسپلانٹ میں خلیے عطیہ دہندہ سے آتے ہیں، اکثر مماثل بھائی یا بہن سے۔ معالج بیماری اور اس کے مرحلے کے مطابق قسم چنتے ہیں۔",
    "در پیوند اتولوگ، سلول‌های بنیادی خود بیمار جمع و نگهداری می‌شوند و پس از درمان با دوز بالا بازگردانده می‌شوند. در پیوند آلوژن سلول‌ها از دهنده می‌آیند، اغلب از برادر یا خواهر سازگار. پزشکان نوع را بر اساس بیماری و مرحلهٔ آن انتخاب می‌کنند.",
)
add("Inherited disorders", "Наследственные болезни", "Trastornos hereditarios", "Maladies héréditaires", "موروثی عوارض", "اختلال‌های ارثی")
add("International patient journey", "Путь иностранного пациента", "Recorrido del paciente internacional", "Parcours du patient international", "بین الاقوامی مریض کا سفر", "مسیر بیمار بین‌المللی")
add(
    "Is a transplant right for my case?",
    "Подходит ли трансплантация в моём случае?",
    "¿Es adecuado un trasplante en mi caso?",
    "Une greffe convient-elle à mon cas ?",
    "کیا ٹرانسپلانٹ میرے کیس کے لیے درست ہے؟",
    "آیا پیوند برای پروندهٔ من مناسب است؟",
)
add("Isolation rooms", "Изоляторы", "Habitaciones de aislamiento", "Chambres d’isolement", "آئسولیشن کمرے", "اتاق‌های ایزوله")
add(
    "It depends on the transplant type and on recovery. Allogeneic transplants usually need a longer stay near the hospital after discharge than autologous transplants, and the team gives you an estimate before you travel.",
    "Это зависит от типа трансплантации и восстановления. После выписки аллогенная трансплантация обычно требует более долгого пребывания рядом с больницей, чем аутологичная, и команда даёт оценку до поездки.",
    "Depende del tipo de trasplante y de la recuperación. Los trasplantes alogénicos suelen necesitar una estancia más larga cerca del hospital tras el alta que los autólogos, y el equipo le da una estimación antes de viajar.",
    "Cela dépend du type de greffe et de la récupération. Les allogreffes demandent en général un séjour plus long près de l’hôpital après la sortie que les autogreffes, et l’équipe vous donne une estimation avant le voyage.",
    "یہ ٹرانسپلانٹ کی قسم اور صحت یابی پر منحصر ہے۔ ایلو جینک ٹرانسپلانٹ کو ڈسچارج کے بعد ہسپتال کے قریب عام طور پر آٹولوگس سے لمبا قیام چاہیے، اور ٹیم سفر سے پہلے تخمینہ دیتی ہے۔",
    "به نوع پیوند و بهبود بستگی دارد. پیوند آلوژن پس از ترخیص معمولاً اقامت طولانی‌تری نزدیک بیمارستان می‌خواهد تا پیوند اتولوگ، و تیم پیش از سفر برآورد می‌دهد.",
)
# fix Russian grammar slip in the previous string - I'll correct below if I notice. "и команду даёт" should be "и команда даёт". I'll fix with a search after write.
add("JACIE accredited center", "Центр с аккредитацией JACIE", "Centro acreditado por JACIE", "Centre accrédité JACIE", "JACIE سے تصدیق شدہ مرکز", "مرکز دارای اعتبار JACIE")
add(
    "Lymphomas (Hodgkin, non-Hodgkin)",
    "Лимфомы (Ходжкина, неходжкинские)",
    "Linfomas (Hodgkin, no Hodgkin)",
    "Lymphomes (Hodgkin, non hodgkiniens)",
    "لمفوما (ہوجکن، نان ہوجکن)",
    "لنفوم (هوچکین، غیرهوچکین)",
)
add("Multiple myeloma", "Множественная миелома", "Mieloma múltiple", "Myélome multiple", "ملٹیپل مائیلوما", "میلوما متعدد")
add("Myelodysplastic syndrome (MDS)", "Миелодиспластический синдром (MDS)", "Síndrome mielodisplásico (MDS)", "Syndrome myélodysplasique (MDS)", "مائیلوڈیسپلاسٹک سنڈروم (MDS)", "سندرم میلودیسپلاستیک (MDS)")
add(
    f"Names, titles and specialties come from the hospital{A}s official physician pages. They are shown for information only: your file is routed to the right specialty and the hospital assigns the treating physician.",
    "Имена, звания и специальности взяты с официальных страниц врачей больницы. Они приведены для сведения: файл направляют в нужный профиль, а лечащего врача назначает больница.",
    "Los nombres, títulos y especialidades proceden de las páginas oficiales de médicos del hospital. Se muestran a título informativo: el expediente se dirige a la especialidad adecuada y el hospital asigna al médico tratante.",
    "Les noms, titres et spécialités viennent des pages officielles des médecins de l’hôpital. Ils sont donnés à titre informatif : le dossier est orienté vers la bonne spécialité et l’hôpital désigne le médecin traitant.",
    "نام، عہدے اور شعبے ہسپتال کے سرکاری معالج صفحات سے لیے گئے ہیں۔ یہ صرف معلومات کے لیے ہیں: فائل درست شعبے کو جاتی ہے اور علاج کرنے والا معالج ہسپتال مقرر کرتا ہے۔",
    "نام، عنوان و تخصص از صفحه‌های رسمی پزشکان بیمارستان است. فقط برای اطلاع نشان داده می‌شوند: پرونده به تخصص درست می‌رود و بیمارستان پزشک معالج را تعیین می‌کند.",
)
add(
    "Not always. The physicians decide after reviewing your file and may suggest another treatment, including treatment closer to home.",
    "Не всегда. Врачи решают после разбора документов и могут предложить другое лечение, в том числе ближе к дому.",
    "No siempre. Los médicos deciden tras revisar el expediente y pueden proponer otro tratamiento, incluido uno más cerca de casa.",
    "Pas toujours. Les médecins décident après l’examen du dossier et peuvent proposer un autre traitement, y compris plus près de chez vous.",
    "ہمیشہ نہیں۔ معالج فائل دیکھ کر فیصلہ کرتے ہیں اور دوسرا علاج تجویز کر سکتے ہیں، بشمول گھر کے قریب علاج۔",
    "همیشه نه. پزشکان پس از بررسی پرونده تصمیم می‌گیرند و ممکن است درمان دیگری پیشنهاد کنند، از جمله درمان نزدیک خانه.",
)
add(
    "On WhatsApp or by email; your coordinator confirms what has arrived.",
    "В WhatsApp или по эл. почте; координатор подтвердит, что получено.",
    "Por WhatsApp o por correo; su coordinador confirma lo que ha llegado.",
    "Par WhatsApp ou par e-mail ; votre coordinateur confirme ce qui est arrivé.",
    "واٹس ایپ یا ای میل پر؛ کوآرڈینیٹر تصدیق کرتا ہے کہ کیا پہنچ گیا۔",
    "در واتس‌اپ یا با ایمیل؛ هماهنگ‌کننده تأیید می‌کند چه چیزی رسیده است.",
)
add(
    "Patient and donor evaluation in Istanbul",
    "Обследование пациента и донора в Стамбуле",
    "Valoración del paciente y del donante en Estambul",
    "Évaluation du patient et du donneur à Istanbul",
    "استنبول میں مریض اور عطیہ دہندہ کا جائزہ",
    "ارزیابی بیمار و دهنده در استانبول",
)
add(
    "Physicians reply in writing: whether a transplant may be an option, which type, and which tests are missing.",
    "Врачи отвечают письменно: может ли трансплантация быть вариантом, какого типа и каких анализов не хватает.",
    "Los médicos responden por escrito: si un trasplante puede ser una opción, de qué tipo y qué pruebas faltan.",
    "Les médecins répondent par écrit : si une greffe peut être une option, de quel type, et quels examens manquent.",
    "معالج تحریری جواب دیتے ہیں: ٹرانسپلانٹ ایک اختیار ہو سکتا ہے یا نہیں، کون سی قسم، اور کون سے ٹیسٹ باقی ہیں۔",
    "پزشکان کتبی پاسخ می‌دهند: آیا پیوند می‌تواند یک گزینه باشد، کدام نوع، و کدام آزمایش‌ها نیست.",
)
add("Plan and invitation letters", "План и пригласительные письма", "Plan y cartas de invitación", "Plan et lettres d’invitation", "منصوبہ اور دعوتی خطوط", "برنامه و نامه‌های دعوت")
add("Primary immunodeficiencies", "Первичные иммунодефициты", "Inmunodeficiencias primarias", "Déficits immunitaires primitifs", "پرائمری امیونو ڈیفیشنسی", "نقص ایمنی اولیه")
add(
    "Proposed dates, an estimate of the stay and medical invitation letters for the patient, the donor and a companion. Costs are assessed case by case.",
    "Предлагаемые даты, оценка длительности пребывания и медицинские приглашения для пациента, донора и сопровождающего. Стоимость оценивают индивидуально.",
    "Fechas propuestas, una estimación de la estancia y cartas de invitación médica para el paciente, el donante y un acompañante. El coste se valora caso por caso.",
    "Dates proposées, une estimation du séjour et des lettres d’invitation médicale pour le patient, le donneur et un accompagnant. Le coût est établi au cas par cas.",
    "تجویز کردہ تاریخیں، قیام کا تخمینہ اور مریض، عطیہ دہندہ اور ساتھی کے لیے طبی دعوتی خطوط۔ لاگت ہر کیس الگ لگائی جاتی ہے۔",
    "تاریخ‌های پیشنهادی، برآورد اقامت و نامه‌های دعوت پزشکی برای بیمار، دهنده و یک همراه. هزینه مورد به مورد برآورد می‌شود.",
)
add("Read about CAR-T", "Читать о CAR-T", "Leer sobre CAR-T", "Lire sur le CAR-T", "CAR-T کے بارے میں پڑھیں", "دربارهٔ CAR-T بخوانید")
add(
    "Recent blood tests and imaging reports (for example PET-CT or CT)",
    "Недавние анализы крови и заключения по снимкам (например, PET-CT или CT)",
    "Análisis de sangre recientes e informes de imagen (por ejemplo PET-CT o TC)",
    "Analyses de sang récentes et comptes rendus d’imagerie (par exemple TEP-TDM ou TDM)",
    "حالیہ خون کے ٹیسٹ اور امیجنگ رپورٹس (مثلاً PET-CT یا CT)",
    "آزمایش خون اخیر و گزارش تصویربرداری (برای مثال PET-CT یا CT)",
)
add("Related centers and pages", "Связанные центры и страницы", "Centros y páginas relacionados", "Centres et pages liés", "متعلقہ مراکز اور صفحات", "مراکز و صفحه‌های مرتبط")
add("Return home and shared follow-up", "Возвращение домой и совместное наблюдение", "Regreso a casa y seguimiento compartido", "Retour à la maison et suivi partagé", "گھر واپسی اور مشترکہ فالو اپ", "بازگشت به خانه و پیگیری مشترک")
add("Review by the transplant team", "Разбор командой трансплантации", "Revisión del equipo de trasplante", "Examen par l’équipe de greffe", "ٹرانسپلانٹ ٹیم کا جائزہ", "بررسی تیم پیوند")
add(
    "Send what you have: photos and scanned copies are fine to start. Your coordinator tells you if the team needs anything else.",
    "Отправьте то, что есть: для начала достаточно фото и сканов. Координатор скажет, если команде нужно ещё что-то.",
    "Envíe lo que tenga: para empezar bastan fotos y copias escaneadas. Su coordinador le dirá si el equipo necesita algo más.",
    "Envoyez ce que vous avez : des photos et des copies numérisées suffisent pour commencer. Votre coordinateur vous dit si l’équipe a besoin d’autre chose.",
    "جو ہے بھیجیں: شروع کے لیے تصویریں اور سکین کاپیاں کافی ہیں۔ کوآرڈینیٹر بتائے گا اگر ٹیم کو کچھ اور چاہیے۔",
    "هر چه دارید بفرستید: برای شروع عکس و نسخهٔ اسکن کافی است. هماهنگ‌کننده می‌گوید اگر تیم چیز دیگری بخواهد.",
)
add("Send your file for a transplant review", "Отправьте документы на разбор перед трансплантацией", "Envíe su expediente para una revisión de trasplante", "Envoyez votre dossier pour un examen de greffe", "ٹرانسپلانٹ جائزے کے لیے فائل بھیجیں", "پرونده را برای بررسی پیوند بفرستید")
add("Send your reports", "Отправьте документы", "Envíe sus informes", "Envoyez vos documents", "رپورٹس بھیجیں", "گزارش‌ها را بفرستید")
add(
    "Send your reports on WhatsApp or by email, or leave your details in the form and a coordinator who speaks your language will contact you. The first file review does not commit you to anything.",
    "Отправьте документы в WhatsApp или по эл. почте либо оставьте контакты в форме, и координатор, который говорит на вашем языке, свяжется с вами. Первичный разбор ни к чему не обязывает.",
    "Envíe sus informes por WhatsApp o por correo, o deje sus datos en el formulario y un coordinador que habla su idioma le contactará. La primera revisión del expediente no le compromete a nada.",
    "Envoyez vos documents par WhatsApp ou par e-mail, ou laissez vos coordonnées dans le formulaire et un coordinateur qui parle votre langue vous contactera. Le premier examen du dossier ne vous engage à rien.",
    "رپورٹس واٹس ایپ یا ای میل پر بھیجیں، یا فارم میں تفصیلات لکھیں اور آپ کی زبان بولنے والا کوآرڈینیٹر رابطہ کرے گا۔ پہلا فائل جائزہ آپ کو کسی چیز کا پابند نہیں کرتا۔",
    "گزارش‌ها را در واتس‌اپ یا با ایمیل بفرستید، یا مشخصات را در فرم بگذارید تا هماهنگ‌کننده‌ای که زبان شما را می‌داند تماس بگیرد. بررسی نخست پرونده شما را به چیزی متعهد نمی‌کند.",
)
add(
    "Stem cell transplants for adults and children with blood cancers and some rare blood and immune disorders, in dedicated isolation units with a multidisciplinary team.",
    "Трансплантация стволовых клеток взрослым и детям с раком крови и некоторыми редкими болезнями крови и иммунитета, в отдельных изоляторах с мультидисциплинарной командой.",
    "Trasplantes de células madre para adultos y niños con cánceres de la sangre y algunos trastornos raros de la sangre y la inmunidad, en unidades de aislamiento dedicadas con un equipo multidisciplinar.",
    "Greffes de cellules souches pour adultes et enfants atteints de cancers du sang et de certaines maladies rares du sang et de l’immunité, dans des unités d’isolement dédiées avec une équipe multidisciplinaire.",
    "خون کے کینسر اور خون و قوتِ مدافعت کے کچھ نایاب عوارض والے بالغوں اور بچوں کے لیے اسٹیم سیل ٹرانسپلانٹ، الگ آئسولیشن یونٹوں میں کثیر الشعبہ ٹیم کے ساتھ۔",
    "پیوند سلول بنیادی برای بزرگسال و کودک با سرطان خون و برخی اختلال‌های نادر خون و ایمنی، در بخش‌های ایزولهٔ اختصاصی با تیم چندتخصصی.",
)
add(
    "Step by step: from sending your report to follow-up at home",
    "Шаг за шагом: от отправки документов до наблюдения дома",
    "Paso a paso: del envío del informe al seguimiento en casa",
    "Étape par étape : de l’envoi du compte rendu au suivi à la maison",
    "قدم بہ قدم: رپورٹ بھیجنے سے گھر کے فالو اپ تک",
    "گام به گام: از ارسال گزارش تا پیگیری در خانه",
)
add(
    "The cells are given by infusion; you stay in an isolation room until the new cells start working.",
    "Клетки вводят инфузией; вы остаётесь в изоляторе, пока новые клетки не начнут работать.",
    "Las células se administran por infusión; permanece en una habitación de aislamiento hasta que las nuevas células empiezan a funcionar.",
    "Les cellules sont administrées par perfusion ; vous restez en chambre d’isolement jusqu’à ce que les nouvelles cellules commencent à agir.",
    "خلیے انفیوژن سے دیے جاتے ہیں؛ آپ آئسولیشن کمرے میں رہتے ہیں جب تک نئے خلیے کام شروع نہ کریں۔",
    "سلول‌ها با انفوزیون داده می‌شوند؛ تا وقتی سلول‌های جدید کار را شروع کنند در اتاق ایزوله می‌مانید.",
)
add(
    "The latest letter or discharge summary from your doctor",
    "Последнее письмо или выписной эпикриз вашего врача",
    "La carta o el informe de alta más reciente de su médico",
    "La dernière lettre ou le compte rendu de sortie de votre médecin",
    "آپ کے ڈاکٹر کا تازہ ترین خط یا ڈسچارج خلاصہ",
    "آخرین نامه یا خلاصهٔ ترخیص پزشک شما",
)
add(
    f"The patient{A}s own cells, collected, stored and returned after treatment.",
    "Собственные клетки пациента: их собирают, сохраняют и возвращают после лечения.",
    "Las células del propio paciente, recogidas, guardadas y devueltas tras el tratamiento.",
    "Les propres cellules du patient, recueillies, conservées et rendues après le traitement.",
    "مریض کے اپنے خلیے، جو جمع کر کے محفوظ کیے جاتے ہیں اور علاج کے بعد واپس دیے جاتے ہیں۔",
    "سلول‌های خود بیمار، که جمع، نگهداری و پس از درمان بازگردانده می‌شوند.",
)
add("Through donor registries", "Через регистры доноров", "A través de registros de donantes", "Par des registres de donneurs", "عطیہ دہندہ رجسٹریوں کے ذریعے", "از راه ثبت‌های دهنده")
add("Transplant and recovery in isolation", "Трансплантация и восстановление в изоляторе", "Trasplante y recuperación en aislamiento", "Greffe et récupération en isolement", "آئسولیشن میں ٹرانسپلانٹ اور صحت یابی", "پیوند و بهبود در ایزوله")
add("Types of transplant", "Виды трансплантации", "Tipos de trasplante", "Types de greffe", "ٹرانسپلانٹ کی اقسام", "انواع پیوند")
add(
    "We do not publish prices. The cost is assessed individually after the medical team has reviewed your report.",
    "Цены мы не публикуем. Стоимость оценивают индивидуально после того, как медицинская команда прочитает заключение.",
    "No publicamos precios. El coste se valora de forma individual después de que el equipo médico haya revisado su informe.",
    "Nous ne publions pas de prix. Le coût est établi individuellement après que l’équipe médicale a examiné votre compte rendu.",
    "ہم قیمتیں شائع نہیں کرتے۔ لاگت میڈیکل ٹیم کے رپورٹ دیکھنے کے بعد ہر شخص کے لیے الگ لگائی جاتی ہے۔",
    "قیمت منتشر نمی‌کنیم. هزینه پس از بررسی گزارش توسط تیم پزشکی، برای هر فرد جداگانه برآورد می‌شود.",
)
add(
    "What is the difference between an autologous and an allogeneic transplant?",
    "В чём разница между аутологичной и аллогенной трансплантацией?",
    "¿Cuál es la diferencia entre un trasplante autólogo y uno alogénico?",
    "Quelle est la différence entre une autogreffe et une allogreffe ?",
    "آٹولوگس اور ایلو جینک ٹرانسپلانٹ میں کیا فرق ہے؟",
    "تفاوت پیوند اتولوگ و آلوژن چیست؟",
)
add("Which documents should I send?", "Какие документы отправить?", "¿Qué documentos debo enviar?", "Quels documents dois-je envoyer ?", "کون سی دستاویزات بھیجوں؟", "کدام مدارک را بفرستم؟")
add(
    "Who may a bone marrow transplant suit?",
    "Кому может подойти трансплантация костного мозга?",
    "¿A quién puede convenir un trasplante de médula ósea?",
    "À qui une greffe de moelle osseuse peut-elle convenir ?",
    "بون میرو ٹرانسپلانٹ کس کے لیے موزوں ہو سکتا ہے؟",
    "پیوند مغز استخوان برای چه کسی ممکن است مناسب باشد؟",
)
add(
    "Yes. Biruni University Hospital has an adult bone marrow transplant center and a separate pediatric bone marrow transplant center.",
    "Да. В Университетской больнице Бируни есть центр трансплантации костного мозга для взрослых и отдельный детский центр.",
    "Sí. El Hospital Universitario Biruni tiene un centro de trasplante de médula ósea de adultos y un centro pediátrico aparte.",
    "Oui. L’Hôpital universitaire Biruni a un centre de greffe de moelle osseuse pour adultes et un centre pédiatrique distinct.",
    "جی ہاں۔ Biruni یونیورسٹی ہسپتال میں بالغوں کا بون میرو ٹرانسپلانٹ مرکز ہے اور الگ بچوں کا مرکز بھی۔",
    "بله. بیمارستان دانشگاه بیرونی مرکز پیوند مغز استخوان بزرگسالان و یک مرکز جداگانهٔ کودکان دارد.",
)
add(
    "Yes. For a related-donor transplant, the donor travels to Istanbul for tests and cell collection, and we help arrange their stay.",
    "Да. При трансплантации от родственного донора он приезжает в Стамбул на обследования и сбор клеток, и мы помогаем организовать пребывание.",
    "Sí. En un trasplante de donante emparentado, el donante viaja a Estambul para las pruebas y la recogida de células, y ayudamos a organizar su estancia.",
    "Oui. Pour une greffe avec donneur apparenté, le donneur se rend à Istanbul pour les examens et le recueil des cellules, et nous aidons à organiser son séjour.",
    "جی ہاں۔ رشتہ دار عطیہ دہندہ والے ٹرانسپلانٹ میں عطیہ دہندہ ٹیسٹوں اور خلیے جمع کرنے کے لیے استنبول آتا ہے، اور ہم اس کے قیام کا بندوبست کرنے میں مدد کرتے ہیں۔",
    "بله. در پیوند از دهندهٔ خویشاوند، دهنده برای آزمایش و جمع‌آوری سلول به استانبول می‌آید و ما برای اقامت او کمک می‌کنیم.",
)
add(
    "depends on the transplant type; allogeneic transplants usually need a longer stay near the hospital after discharge.",
    "зависит от типа трансплантации; аллогенная обычно требует более долгого пребывания рядом с больницей после выписки.",
    "depende del tipo de trasplante; los alogénicos suelen necesitar una estancia más larga cerca del hospital tras el alta.",
    "dépend du type de greffe ; les allogreffes demandent en général un séjour plus long près de l’hôpital après la sortie.",
    "ٹرانسپلانٹ کی قسم پر منحصر ہے؛ ایلو جینک ٹرانسپلانٹ کو ڈسچارج کے بعد ہسپتال کے قریب عام طور پر لمبا قیام چاہیے۔",
    "به نوع پیوند بستگی دارد؛ پیوند آلوژن پس از ترخیص معمولاً اقامت طولانی‌تری نزدیک بیمارستان می‌خواهد.",
)
add(
    "is also available at Biruni University Hospital for eligible patients, within the hematology and transplant program.",
    "также доступна в Университетской больнице Бируни для подходящих пациентов, в рамках программы гематологии и трансплантации.",
    "también está disponible en el Hospital Universitario Biruni para pacientes candidatos, dentro del programa de hematología y trasplante.",
    "est aussi disponible à l’Hôpital universitaire Biruni pour les patients éligibles, dans le programme d’hématologie et de greffe.",
    "اہل مریضوں کے لیے Biruni یونیورسٹی ہسپتال میں ہیماٹولوجی اور ٹرانسپلانٹ پروگرام کے اندر بھی دستیاب ہے۔",
    "برای بیماران واجد شرایط در بیمارستان دانشگاه بیرونی، در برنامهٔ خون‌شناسی و پیوند، نیز در دسترس است.",
)
add("transplant types", "виды трансплантации", "tipos de trasplante", "types de greffe", "ٹرانسپلانٹ کی اقسام", "انواع پیوند")
add("two dedicated units", "два отдельных отделения", "dos unidades dedicadas", "deux unités dédiées", "دو الگ یونٹ", "دو بخش اختصاصی")
add(
    "with infection-control systems",
    "с системами контроля инфекций",
    "con sistemas de control de infecciones",
    "avec des systèmes de contrôle des infections",
    "انفیکشن کنٹرول کے نظام کے ساتھ",
    "با سامانه‌های کنترل عفونت",
)
add(
    "Autologous and allogeneic bone marrow (stem cell) transplant for adults and children at Biruni University Hospital, Istanbul. Send your reports for a review.",
    "Аутологичная и аллогенная трансплантация костного мозга (стволовых клеток) взрослым и детям в Университетской больнице Бируни в Стамбуле. Отправьте документы на разбор.",
    "Trasplante de médula ósea (células madre) autólogo y alogénico para adultos y niños en el Hospital Universitario Biruni de Estambul. Envíe sus informes para una revisión.",
    "Greffe de moelle osseuse (cellules souches) autologue et allogénique pour adultes et enfants à l’Hôpital universitaire Biruni, à Istanbul. Envoyez vos documents pour un examen.",
    "استنبول کے Biruni یونیورسٹی ہسپتال میں بالغوں اور بچوں کے لیے آٹولوگس اور ایلو جینک بون میرو (اسٹیم سیل) ٹرانسپلانٹ۔ جائزے کے لیے رپورٹس بھیجیں۔",
    "پیوند مغز استخوان (سلول بنیادی) اتولوگ و آلوژن برای بزرگسال و کودک در بیمارستان دانشگاه بیرونی، استانبول. گزارش‌ها را برای بررسی بفرستید.",
)

from rest_centers_more import load as _load_more
from rest_centers_tail import load as _load_tail

_load_more(add, same)
_load_tail(add, same)
add(
    "Bone Marrow Transplant in Istanbul, Turkey | Biruni Bridge",
    "Трансплантация костного мозга в Стамбуле, Турция | Biruni Bridge",
    "Trasplante de médula ósea en Estambul, Turquía | Biruni Bridge",
    "Greffe de moelle osseuse à Istanbul, Turquie | Biruni Bridge",
    "استنبول، ترکی میں بون میرو ٹرانسپلانٹ | Biruni Bridge",
    "پیوند مغز استخوان در استانبول، ترکیه | Biruni Bridge",
)
add(
    "Bone marrow transplant in Istanbul for adults and children",
    "Трансплантация костного мозга в Стамбуле для взрослых и детей",
    "Trasplante de médula ósea en Estambul para adultos y niños",
    "Greffe de moelle osseuse à Istanbul pour adultes et enfants",
    "بالغوں اور بچوں کے لیے استنبول میں بون میرو ٹرانسپلانٹ",
    "پیوند مغز استخوان در استانبول برای بزرگسال و کودک",
)
add(
    f"As stated on the Bone Marrow Transplant Center page of the hospital{A}s website.",
    "Как указано на странице центра трансплантации костного мозга на сайте больницы.",
    "Como figura en la página del centro de trasplante de médula ósea del sitio del hospital.",
    "Comme indiqué sur la page du centre de greffe de moelle osseuse du site de l’hôpital.",
    "جیسا ہسپتال کی ویب سائٹ پر بون میرو ٹرانسپلانٹ مرکز کے صفحے پر درج ہے۔",
    "همان‌گونه که در صفحهٔ مرکز پیوند مغز استخوان در وب‌سایت بیمارستان آمده است.",
)
add(
    "The Bone Marrow Transplant Center provides stem cell transplants for adults and children with blood cancers and rare immune disorders. The program covers patient and donor evaluation, conditioning, transplant in isolation rooms, and aftercare.",
    "Центр трансплантации костного мозга проводит трансплантацию стволовых клеток взрослым и детям с раком крови и редкими иммунными нарушениями. Программа включает обследование пациента и донора, кондиционирование, трансплантацию в изоляторах и последующее наблюдение.",
    "El centro de trasplante de médula ósea realiza trasplantes de células madre en adultos y niños con cánceres de la sangre y trastornos inmunitarios raros. El programa cubre la valoración del paciente y del donante, el acondicionamiento, el trasplante en habitaciones de aislamiento y el seguimiento.",
    "Le centre de greffe de moelle osseuse réalise des greffes de cellules souches chez l’adulte et l’enfant atteints de cancers du sang et de troubles immunitaires rares. Le programme couvre l’évaluation du patient et du donneur, le conditionnement, la greffe en chambre d’isolement et le suivi.",
    "بون میرو ٹرانسپلانٹ مرکز خون کے کینسر اور نایاب مدافعتی عوارض والے بالغوں اور بچوں کا اسٹیم سیل ٹرانسپلانٹ کرتا ہے۔ پروگرام میں مریض اور عطیہ دہندہ کا جائزہ، کنڈیشننگ، آئسولیشن کمرے میں ٹرانسپلانٹ اور بعد کی دیکھ بھال شامل ہے۔",
    "مرکز پیوند مغز استخوان پیوند سلول بنیادی را برای بزرگسال و کودک با سرطان خون و اختلال ایمنی نادر انجام می‌دهد. برنامه ارزیابی بیمار و دهنده، آماده‌سازی، پیوند در اتاق ایزوله و مراقبت بعدی را در بر می‌گیرد.",
)
add(
    "Send your medical report for a physician review before you book anything",
    "Отправьте медицинское заключение на разбор врачом до того, как что-либо бронировать",
    "Envíe su informe médico para una revisión por un médico antes de reservar nada",
    "Envoyez votre compte rendu médical pour un examen par un médecin avant toute réservation",
    "کچھ بک کرنے سے پہلے معالج کے جائزے کے لیے میڈیکل رپورٹ بھیجیں",
    "پیش از هر رزروی گزارش پزشکی را برای بررسی پزشک بفرستید",
)
add(
    "Bone marrow transplant and hematology physicians",
    "Врачи трансплантации костного мозга и гематологии",
    "Médicos de trasplante de médula ósea y hematología",
    "Médecins de greffe de moelle osseuse et d’hématologie",
    "بون میرو ٹرانسپلانٹ اور ہیماٹولوجی کے معالج",
    "پزشکان پیوند مغز استخوان و خون‌شناسی",
)
add(
    "Pediatric hematology & oncology: Prof. Dr. Hilmi Apak and Asst. Prof. Dr. Ömer Doğru",
    "Детская гематология и онкология: Prof. Dr. Hilmi Apak и Asst. Prof. Dr. Ömer Doğru",
    "Hematología y oncología pediátricas: Prof. Dr. Hilmi Apak y Asst. Prof. Dr. Ömer Doğru",
    "Hématologie et oncologie pédiatriques : Prof. Dr. Hilmi Apak et Asst. Prof. Dr. Ömer Doğru",
    "بچوں کے امراضِ خون اور آنکولوجی: Prof. Dr. Hilmi Apak اور Asst. Prof. Dr. Ömer Doğru",
    "خون و انکولوژی کودکان: Prof. Dr. Hilmi Apak و Asst. Prof. Dr. Ömer Doğru",
)
add(
    "Nuclear medicine and molecular imaging",
    "Ядерная медицина и молекулярная визуализация",
    "Medicina nuclear e imagen molecular",
    "Médecine nucléaire et imagerie moléculaire",
    "نیوکلیئر میڈیسن اور مالیکیولر امیجنگ",
    "پزشکی هسته‌ای و تصویربرداری مولکولی",
)
add(
    "Nuclear medicine uses small amounts of radioactive tracers to image how organs work, and to treat some conditions. It is central to staging many cancers and following response to treatment.",
    "Ядерная медицина использует небольшие количества радиоактивных индикаторов, чтобы видеть, как работают органы, и лечить некоторые состояния. Она важна для стадирования многих видов рака и оценки ответа на лечение.",
    "La medicina nuclear usa pequeñas cantidades de trazadores radiactivos para ver cómo funcionan los órganos y para tratar algunas afecciones. Es central para estadificar muchos cánceres y seguir la respuesta al tratamiento.",
    "La médecine nucléaire utilise de petites quantités de traceurs radioactifs pour voir comment les organes fonctionnent et pour traiter certaines affections. Elle est centrale pour stadifier de nombreux cancers et suivre la réponse au traitement.",
    "نیوکلیئر میڈیسن تھوڑی مقدار میں تابکار ٹریسر استعمال کرتی ہے تاکہ دیکھا جائے اعضاء کیسے کام کرتے ہیں، اور کچھ حالتوں کا علاج کیا جائے۔ یہ کئی کینسر کی درجہ بندی اور علاج کے جواب کی پیروی کے لیے مرکزی ہے۔",
    "پزشکی هسته‌ای مقدار کمی ردیاب پرتوزا به کار می‌برد تا کار اعضا دیده شود و برخی وضعیت‌ها درمان شوند. برای مرحله‌بندی بسیاری از سرطان‌ها و پیگیری پاسخ به درمان نقش محوری دارد.",
)
add(
    "Organ Transplant Center: kidney and liver",
    "Центр трансплантации органов: почка и печень",
    "Centro de trasplante de órganos: riñón e hígado",
    "Centre de transplantation d’organes : rein et foie",
    "اعضا کے ٹرانسپلانٹ کا مرکز: گردہ اور جگر",
    "مرکز پیوند اعضا: کلیه و کبد",
)
add(
    "The Organ Transplant Center is licensed by the Ministry of Health for kidney and liver transplantation. Everything follows Turkish law: no transplant goes ahead without donor and recipient evaluation, proof of relationship and ethics-committee approval where required.",
    "Центр трансплантации органов лицензирован Министерством здравоохранения для трансплантации почки и печени. Всё идёт по закону Турции: трансплантация не проводится без обследования донора и реципиента, подтверждения родства и, где требуется, одобрения этического комитета.",
    "El centro de trasplante de órganos tiene licencia del Ministerio de Salud para el trasplante de riñón e hígado. Todo sigue la ley turca: ningún trasplante sigue adelante sin la valoración del donante y del receptor, la prueba del parentesco y, cuando se exige, la aprobación del comité de ética.",
    "Le centre de transplantation d’organes est autorisé par le ministère de la Santé pour la transplantation rénale et hépatique. Tout suit le droit turc : aucune greffe n’a lieu sans évaluation du donneur et du receveur, preuve du lien et, lorsque c’est exigé, approbation du comité d’éthique.",
    "اعضا کے ٹرانسپلانٹ کا مرکز گردے اور جگر کی پیوند کاری کے لیے وزارت صحت سے لائسنس یافتہ ہے۔ سب کچھ ترکی کے قانون کے مطابق ہوتا ہے: عطیہ دہندہ اور وصول کنندہ کے جائزے، رشتے کے ثبوت اور جہاں ضروری ہو اخلاقیات کمیٹی کی منظوری کے بغیر کوئی ٹرانسپلانٹ آگے نہیں بڑھتا۔",
    "مرکز پیوند اعضا برای پیوند کلیه و کبد از وزارت بهداشت مجوز دارد. همه چیز طبق قانون ترکیه است: هیچ پیوندی بدون ارزیابی دهنده و گیرنده، اثبات رابطه و، جایی که لازم است، تأیید کمیتهٔ اخلاق پیش نمی‌رود.",
)
add(
    "and Spine Health Center",
    "и Центр здоровья позвоночника",
    "y Centro de salud de la columna",
    "et Centre de santé du rachis",
    "اور ریڑھ کی ہڈی کا مرکز",
    "و مرکز سلامت ستون فقرات",
)
