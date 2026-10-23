"""IVF through surgical oncology, plus page titles."""

from __future__ import annotations

A = "\u2019"


def load(add, same) -> None:
    # IVF
    add("All related physicians in the directory (2)", "Все связанные врачи в справочнике (2)", "Todos los médicos relacionados en el directorio (2)", "Tous les médecins concernés dans l’annuaire (2)", "ڈائریکٹری میں تمام متعلقہ معالج (2)", "همهٔ پزشکان مرتبط در فهرست (۲)")
    add("And semen analysis.", "И анализ спермы.", "Y análisis de semen.", "Et spermogramme.", "اور منی کا تجزیہ۔", "و آزمایش مایع منی.")
    add("By vitrification.", "Витрификацией.", "Por vitrificación.", "Par vitrification.", "وٹریفیکیشن سے۔", "با ویتریفیکاسیون.")
    add("Can donor eggs be used?", "Можно ли использовать донорские яйцеклетки?", "¿Se pueden usar óvulos de donante?", "Des ovocytes de donneuse peuvent-ils être utilisés ?", "کیا عطیہ دہندہ کے انڈے استعمال ہو سکتے ہیں؟", "آیا تخمک اهداکننده قابل استفاده است؟")
    add("Do you publish success rates?", "Публикуете ли вы показатели результата?", "¿Publican tasas de resultado?", "Publiez-vous des taux de résultat ?", "کیا آپ نتائج کی شرح شائع کرتے ہیں؟", "آیا نرخ نتیجه منتشر می‌کنید؟")
    add("Egg & embryo freezing", "Заморозка яйцеклеток и эмбрионов", "Congelación de óvulos y embriones", "Congélation d’ovocytes et d’embryons", "انڈے اور جنین منجمد کرنا", "انجماد تخمک و جنین")
    add("Egg retrieval & fertilization", "Пункция яйцеклеток и оплодотворение", "Punción ovárica y fecundación", "Ponction ovocytaire et fécondation", "انڈے نکالنا اور فرٹیلائزیشن", "تخمک‌گیری و لقاح")
    add("Embryo genetic screening", "Генетическое исследование эмбрионов", "Estudio genético de embriones", "Examen génétique des embryons", "جنین کی جینیاتی جانچ", "غربالگری ژنتیک جنین")
    add("For both partners.", "Для обоих партнёров.", "Para ambos miembros de la pareja.", "Pour les deux partenaires.", "دونوں ساتھیوں کے لیے۔", "برای هر دو طرف.")
    add("High-risk pregnancy", "Беременность высокого риска", "Embarazo de alto riesgo", "Grossesse à risque élevé", "زیادہ خطرے والی حمل", "بارداری پرخطر")
    add("Hormonal assessment & stimulation", "Гормональная оценка и стимуляция", "Valoración hormonal y estimulación", "Évaluation hormonale et stimulation", "ہارمونل جائزہ اور تحریک", "ارزیابی هورمونی و تحریک")
    add("How long do we stay in Istanbul?", "Как долго мы пробудем в Стамбуле?", "¿Cuánto tiempo estaremos en Estambul?", "Combien de temps resterons-nous à Istanbul ?", "ہم استنبول میں کتنی دیر رہیں گے؟", "چه مدت در استانبول می‌مانیم؟")
    same("ICSI / IVF")
    add("ICSI / classic IVF", "ICSI / классическое ЭКО", "ICSI / FIV clásica", "ICSI / FIV classique", "ICSI / کلاسک IVF", "ICSI / IVF کلاسیک")
    add("IVF & fertility services", "ЭКО и лечение бесплодия", "FIV y servicios de fertilidad", "FIV et soins de fertilité", "IVF اور زرخیزی کی خدمات", "IVF و خدمات باروری")
    add(f"IVF and women{A}s health", "ЭКО и женское здоровье", "FIV y salud de la mujer", "FIV et santé des femmes", "IVF اور خواتین کی صحت", "IVF و سلامت زنان")
    add(f"IVF & women{A}s health in Istanbul | Biruni Bridge", "ЭКО и женское здоровье в Стамбуле | Biruni Bridge", "FIV y salud de la mujer en Estambul | Biruni Bridge", "FIV et santé des femmes à Istanbul | Biruni Bridge", "استنبول میں IVF اور خواتین کی صحت | Biruni Bridge", "IVF و سلامت زنان در استانبول | Biruni Bridge")
    add("In Istanbul.", "В Стамбуле.", "En Estambul.", "À Istanbul.", "استنبول میں۔", "در استانبول.")
    add(
        f"In Türkiye, IVF is carried out only for married couples using the wife{A}s eggs and the husband{A}s sperm. Donor eggs, sperm or embryos and surrogacy are not permitted, and sex selection is not performed except for medical reasons.",
        "В Турции ЭКО проводят только супружеским парам с яйцеклетками жены и спермой мужа. Донорские яйцеклетки, сперма или эмбрионы и суррогатное материнство не разрешены, а выбор пола не проводят, кроме медицинских причин.",
        "En Turquía, la FIV se realiza solo en parejas casadas con los óvulos de la esposa y el esperma del esposo. No están permitidos los óvulos, el esperma o los embriones de donante ni la gestación subrogada, y no se selecciona el sexo salvo por razones médicas.",
        "En Turquie, la FIV n’est pratiquée que pour les couples mariés avec les ovocytes de l’épouse et les spermatozoïdes de l’époux. Les ovocytes, spermatozoïdes ou embryons de donneur et la gestation pour autrui ne sont pas autorisés, et la sélection du sexe n’est pas pratiquée sauf pour des raisons médicales.",
        "ترکی میں IVF صرف شادی شدہ جوڑوں کے لیے ہوتا ہے، بیوی کے انڈوں اور شوہر کے نطفے سے۔ عطیہ دہندہ کے انڈے، نطفہ یا جنین اور سروگیسی کی اجازت نہیں، اور طبی وجہ کے سوا جنس کا انتخاب نہیں ہوتا۔",
        "در ترکیه IVF فقط برای زوج‌های متأهل با تخمک همسر و اسپرم شوهر انجام می‌شود. تخمک، اسپرم یا جنین اهداکننده و رحم جایگزین مجاز نیست، و انتخاب جنس جز به دلایل پزشکی انجام نمی‌شود.",
    )
    add("It depends on the protocol and whether stimulation can start at home.", "Это зависит от протокола и от того, можно ли начать стимуляцию дома.", "Depende del protocolo y de si la estimulación puede empezar en casa.", "Cela dépend du protocole et de la possibilité de commencer la stimulation à la maison.", "یہ پروٹوکول پر منحصر ہے اور اس پر کہ تحریک گھر سے شروع ہو سکتی ہے یا نہیں۔", "به پروتکل بستگی دارد و به اینکه تحریک می‌تواند در خانه شروع شود یا نه.")
    add("Male infertility workup", "Обследование мужского бесплодия", "Estudio de infertilidad masculina", "Bilan d’infertilité masculine", "مردانہ بانجھ پن کا جائزہ", "بررسی ناباروری مرد")
    add("May start at home", "Может начаться дома", "Puede empezar en casa", "Peut commencer à la maison", "گھر سے شروع ہو سکتی ہے", "ممکن است در خانه شروع شود")
    add("Menopause & hormonal disorders", "Менопауза и гормональные нарушения", "Menopausia y trastornos hormonales", "Ménopause et troubles hormonaux", "ماہواری بند ہونا اور ہارمونل عوارض", "یائسگی و اختلال هورمونی")
    add("No, Turkish law does not allow it.", "Нет, закон Турции этого не разрешает.", "No, la ley turca no lo permite.", "Non, le droit turc ne l’autorise pas.", "نہیں، ترکی کا قانون اس کی اجازت نہیں دیتا۔", "نه، قانون ترکیه آن را اجازه نمی‌دهد.")
    same("PGT-A / PGT-M")
    add("PGT-A / PGT-M for medical reasons.", "PGT-A / PGT-M по медицинским причинам.", "PGT-A / PGT-M por razones médicas.", "PGT-A / PGT-M pour des raisons médicales.", "طبی وجوہات کے لیے PGT-A / PGT-M۔", "PGT-A / PGT-M به دلایل پزشکی.")
    add("Pelvic floor disorders", "Болезни тазового дна", "Trastornos del suelo pélvico", "Troubles du plancher pelvien", "شرونی کے فرش کے عوارض", "اختلال کف لگن")
    add("Report review", "Разбор заключения", "Revisión del informe", "Examen du compte rendu", "رپورٹ کا جائزہ", "بررسی گزارش")
    add("Stimulation", "Стимуляция", "Estimulación", "Stimulation", "تحریک", "تحریک")
    add("The IVF journey", "Путь ЭКО", "El recorrido de la FIV", "Le parcours de FIV", "IVF کا سفر", "مسیر IVF")
    add(
        "The center assesses both partners together, plans suitable stimulation and runs an IVF laboratory. We do not publish success rates: results depend on age, cause and many factors your physician explains.",
        "Центр оценивает обоих партнёров вместе, планирует подходящую стимуляцию и ведёт лабораторию ЭКО. Показатели результата мы не публикуем: они зависят от возраста, причины и многих факторов, которые объясняет врач.",
        "El centro valora a ambos miembros de la pareja juntos, planifica una estimulación adecuada y tiene un laboratorio de FIV. No publicamos tasas de resultado: dependen de la edad, la causa y muchos factores que explica su médico.",
        "Le centre évalue les deux partenaires ensemble, planifie une stimulation adaptée et dispose d’un laboratoire de FIV. Nous ne publions pas de taux de résultat : ils dépendent de l’âge, de la cause et de nombreux facteurs que votre médecin explique.",
        "مرکز دونوں ساتھیوں کا جائزہ ایک ساتھ لیتا ہے، موزوں تحریک کی منصوبہ بندی کرتا ہے اور IVF لیبارٹری چلاتا ہے۔ ہم نتائج کی شرح شائع نہیں کرتے: نتیجہ عمر، وجہ اور کئی عوامل پر منحصر ہے جو معالج بتاتا ہے۔",
        "مرکز هر دو طرف را با هم ارزیابی می‌کند، تحریک مناسب را برنامه‌ریزی می‌کند و آزمایشگاه IVF دارد. نرخ نتیجه منتشر نمی‌کنیم: نتیجه به سن، علت و عوامل زیادی بستگی دارد که پزشک توضیح می‌دهد.",
    )
    add("Then a pregnancy test.", "Затем тест на беременность.", "Luego una prueba de embarazo.", "Puis un test de grossesse.", "پھر حمل کا ٹیسٹ۔", "سپس آزمایش بارداری.")
    add("Transfer & follow-up", "Перенос и наблюдение", "Transferencia y seguimiento", "Transfert et suivi", "منتقلی اور فالو اپ", "انتقال و پیگیری")
    add("Vitrification", "Витрификация", "Vitrificación", "Vitrification", "وٹریفیکیشن", "ویتریفیکاسیون")
    add(
        "We do not publish general figures; the physician explains your chances based on your case.",
        "Общие цифры мы не публикуем; врач объясняет перспективы по вашему случаю.",
        "No publicamos cifras generales; el médico explica sus posibilidades según su caso.",
        "Nous ne publions pas de chiffres généraux ; le médecin explique vos chances selon votre cas.",
        "ہم عمومی اعداد شائع نہیں کرتے؛ معالج آپ کے کیس کی بنیاد پر امکانات بتاتا ہے۔",
        "رقم کلی منتشر نمی‌کنیم؛ پزشک شانس شما را بر اساس پرونده توضیح می‌دهد.",
    )
    add("What Turkish law allows", "Что разрешает закон Турции", "Lo que permite la ley turca", "Ce que permet le droit turc", "ترکی کا قانون کیا اجازت دیتا ہے", "آنچه قانون ترکیه اجازه می‌دهد")
    add(f"Women{A}s health services at the center.", "Услуги женского здоровья в центре.", "Servicios de salud de la mujer en el centro.", "Soins de santé des femmes au centre.", "مرکز میں خواتین کی صحت کی خدمات۔", "خدمات سلامت زنان در مرکز.")
    add("egg & embryo freezing", "заморозка яйцеклеток и эмбрионов", "congelación de óvulos y embriones", "congélation d’ovocytes et d’embryons", "انڈے اور جنین منجمد کرنا", "انجماد تخمک و جنین")
    add("embryo genetic testing", "генетическое исследование эмбрионов", "estudio genético de embriones", "examen génétique des embryons", "جنین کا جینیاتی ٹیسٹ", "آزمایش ژنتیک جنین")
    add("in vitro fertilization", "экстракорпоральное оплодотворение", "fecundación in vitro", "fécondation in vitro", "ان ویٹرو فرٹیلائزیشن", "لقاح آزمایشگاهی")

    # Neurosurgery
    add("100+ beds", "более 100 коек", "más de 100 camas", "plus de 100 lits", "100 سے زیادہ بستر", "بیش از ۱۰۰ تخت")
    add("3T MRI and modern CT.", "3T MRI и современная КТ.", "3T MRI y TC moderna.", "3T MRI et TDM moderne.", "3T MRI اور جدید CT۔", "3T MRI و CT امروزی.")
    add("Brain", "Головной мозг", "Cerebro", "Cerveau", "دماغ", "مغز")
    add("Brain, nerve and spine surgery", "Хирургия головного мозга, нервов и позвоночника", "Cirugía de cerebro, nervios y columna", "Chirurgie du cerveau, des nerfs et du rachis", "دماغ، اعصاب اور ریڑھ کی سرجری", "جراحی مغز، عصب و ستون فقرات")
    add("Can my case be assessed from MRI alone?", "Можно ли оценить мой случай только по МРТ?", "¿Mi caso puede valorarse solo con la resonancia?", "Mon cas peut-il être évalué à partir de l’IRM seule ?", "کیا میرا کیس صرف MRI سے دیکھا جا سکتا ہے؟", "آیا پروندهٔ من فقط با MRI ارزیابی می‌شود؟")
    add("Disc herniation", "Грыжа диска", "Hernia discal", "Hernie discale", "ڈسک کا نکلنا", "فتق دیسک")
    add("For complex cases.", "Для сложных случаев.", "Para casos complejos.", "Pour les cas complexes.", "پیچیدہ کیسوں کے لیے۔", "برای موارد پیچیده.")
    add("Fractures", "Переломы", "Fracturas", "Fractures", "فریکچر", "شکستگی")
    add("How long will I stay after brain surgery?", "Как долго я пробуду после операции на мозге?", "¿Cuánto tiempo estaré después de una cirugía cerebral?", "Combien de temps resterai-je après une chirurgie du cerveau ?", "دماغ کی سرجری کے بعد میں کتنی دیر رہوں گا/گی؟", "پس از جراحی مغز چه مدت می‌مانم؟")
    add("How we plan", "Как мы планируем", "Cómo planificamos", "Comment nous planifions", "ہم کیسے منصوبہ بناتے ہیں", "چگونه برنامه‌ریزی می‌کنیم")
    add("Hybrid operating room", "Гибридная операционная", "Quirófano híbrido", "Salle d’opération hybride", "ہائبرڈ آپریٹنگ روم", "اتاق عمل هیبرید")
    add("Hydrocephalus", "Гидроцефалия", "Hidrocefalia", "Hydrocéphalie", "ہائیڈروسیفالس", "هیدروسفالی")
    add("Is surgery always needed for a herniated disc?", "Всегда ли нужна операция при грыже диска?", "¿La cirugía es siempre necesaria en una hernia discal?", "La chirurgie est-elle toujours nécessaire pour une hernie discale ?", "کیا ڈسک ہرنی کے لیے سرجری ہمیشہ ضروری ہے؟", "آیا برای فتق دیسک همیشه جراحی لازم است؟")
    add("It depends on the surgery and recovery.", "Это зависит от операции и восстановления.", "Depende de la cirugía y de la recuperación.", "Cela dépend de la chirurgie et de la récupération.", "یہ سرجری اور صحت یابی پر منحصر ہے۔", "به جراحی و بهبود بستگی دارد.")
    add("It is often enough for a first assessment; more tests may be requested.", "Для первичной оценки этого часто достаточно; могут попросить дополнительные обследования.", "A menudo basta para una primera valoración; pueden pedirse más pruebas.", "Cela suffit souvent pour une première évaluation ; d’autres examens peuvent être demandés.", "پہلے جائزے کے لیے یہ اکثر کافی ہوتا ہے؛ مزید ٹیسٹ مانگے جا سکتے ہیں۔", "برای ارزیابی نخست اغلب کافی است؛ ممکن است آزمایش بیشتر خواسته شود.")
    same("MAGNETOM Vida")
    add("Nerve entrapment", "Ущемление нерва", "Atrapamiento nervioso", "Compression nerveuse", "اعصاب دب جانا", "گیر افتادن عصب")
    add("Nerve injuries", "Травмы нервов", "Lesiones nerviosas", "Lésions nerveuses", "اعصاب کی چوٹیں", "آسیب عصب")
    add(
        "Neurosurgeons review your MRI and reports, and tumor cases are discussed at the tumor board. We explain when surgery is needed and when medication or monitoring is enough.",
        "Нейрохирурги смотрят МРТ и заключения, а опухолевые случаи обсуждает онкоконсилиум. Мы объясняем, когда нужна операция и когда достаточно лекарств или наблюдения.",
        "Los neurocirujanos revisan su resonancia y sus informes, y los casos de tumor se comentan en el comité de tumores. Explicamos cuándo hace falta cirugía y cuándo bastan la medicación o el seguimiento.",
        "Les neurochirurgiens examinent votre IRM et vos comptes rendus, et les cas de tumeur sont discutés en réunion de concertation. Nous expliquons quand la chirurgie est nécessaire et quand un médicament ou une surveillance suffit.",
        "نیورو سرجن آپ کی MRI اور رپورٹس دیکھتے ہیں، اور ٹیومر کے کیس ٹیومر بورڈ میں زیر بحث آتے ہیں۔ ہم بتاتے ہیں کہ سرجری کب ضروری ہے اور دوا یا نگرانی کب کافی ہے۔",
        "جراحان مغز و اعصاب MRI و گزارش‌ها را می‌بینند و موارد تومور در بورد تومور مطرح می‌شود. توضیح می‌دهیم جراحی چه وقت لازم است و دارو یا پایش چه وقت کافی است.",
    )
    add("Neurosurgery in Istanbul | Biruni Bridge", "Нейрохирургия в Стамбуле | Biruni Bridge", "Neurocirugía en Estambul | Biruni Bridge", "Neurochirurgie à Istanbul | Biruni Bridge", "استنبول میں نیورو سرجری | Biruni Bridge", "جراحی مغز و اعصاب در استانبول | Biruni Bridge")
    add("No. Many cases improve without surgery.", "Нет. Многие случаи улучшаются без операции.", "No. Muchos casos mejoran sin cirugía.", "Non. De nombreux cas s’améliorent sans chirurgie.", "نہیں۔ کئی کیس سرجری کے بغیر بہتر ہوتے ہیں۔", "نه. بسیاری موارد بدون جراحی بهتر می‌شوند.")
    add("Peripheral nerves", "Периферические нервы", "Nervios periféricos", "Nerfs périphériques", "بیرونی اعصاب", "اعصاب محیطی")
    add("Physiotherapy after surgery.", "Физиотерапия после операции.", "Fisioterapia después de la cirugía.", "Kinésithérapie après la chirurgie.", "سرجری کے بعد فزیوتھراپی۔", "فیزیوتراپی پس از جراحی.")
    add("Precise imaging", "Точная визуализация", "Imagen precisa", "Imagerie précise", "درست امیجنگ", "تصویربرداری دقیق")
    add("Selected vascular conditions", "Отдельные сосудистые состояния", "Afecciones vasculares seleccionadas", "Certaines affections vasculaires", "منتخب عروقی حالتیں", "برخی وضعیت‌های عروقی")
    add("Send your MRI and reports", "Отправьте МРТ и заключения", "Envíe su resonancia e informes", "Envoyez votre IRM et vos comptes rendus", "MRI اور رپورٹس بھیجیں", "MRI و گزارش‌ها را بفرستید")
    add("Shared decision", "Совместное решение", "Decisión compartida", "Décision partagée", "مشترکہ فیصلہ", "تصمیم مشترک")
    add("Spinal stenosis", "Стеноз позвоночного канала", "Estenosis de canal", "Sténose du canal rachidien", "ریڑھ کی نالی کا تنگ ہونا", "تنگی کانال نخاع")
    add("Spinal tumors", "Опухоли позвоночника", "Tumores de la columna", "Tumeurs rachidiennes", "ریڑھ کے ٹیومر", "تومور ستون فقرات")
    add("With neurology, oncology and radiology.", "С неврологией, онкологией и радиологией.", "Con neurología, oncología y radiología.", "Avec la neurologie, l’oncologie et la radiologie.", "نیورولوجی، آنکولوجی اور ریڈیولوجی کے ساتھ۔", "با نورولوژی، انکولوژی و رادیولوژی.")
    add("for neurosurgery", "для нейрохирургии", "para neurocirugía", "pour la neurochirurgie", "نیورو سرجری کے لیے", "برای جراحی مغز و اعصاب")

    # Nuclear medicine
    add("A PET/CT day", "День PET/CT", "Un día de PET/CT", "Une journée de TEP/TDM", "PET/CT کا ایک دن", "یک روز PET/CT")
    add("All related physicians in the directory (4)", "Все связанные врачи в справочнике (4)", "Todos los médicos relacionados en el directorio (4)", "Tous les médecins concernés dans l’annuaire (4)", "ڈائریکٹری میں تمام متعلقہ معالج (4)", "همهٔ پزشکان مرتبط در فهرست (۴)")
    add("Bone, heart and thyroid studies.", "Исследования костей, сердца и щитовидной железы.", "Estudios de hueso, corazón y tiroides.", "Examens de l’os, du cœur et de la thyroïde.", "ہڈی، دل اور تھائرائیڈ کے معائنے۔", "بررسی استخوان، قلب و تیروئید.")
    add("Brain imaging", "Визуализация мозга", "Imagen cerebral", "Imagerie cérébrale", "دماغ کی امیجنگ", "تصویربرداری مغز")
    add("Can it be compared with a previous scan from home?", "Можно ли сравнить со снимком, сделанным дома?", "¿Se puede comparar con un estudio previo hecho en casa?", "Peut-on le comparer à un examen antérieur fait chez vous ?", "کیا اس کا موازنہ گھر کے پچھلے اسکین سے ہو سکتا ہے؟", "آیا با اسکن قبلی انجام‌شده در خانه مقایسه می‌شود؟")
    add("Cancer staging and response assessment.", "Стадирование рака и оценка ответа.", "Estadificación del cáncer y valoración de la respuesta.", "Stadification du cancer et évaluation de la réponse.", "کینسر کی درجہ بندی اور جواب کا جائزہ۔", "مرحله‌بندی سرطان و ارزیابی پاسخ.")
    add("Cardiac imaging", "Визуализация сердца", "Imagen cardíaca", "Imagerie cardiaque", "دل کی امیجنگ", "تصویربرداری قلب")
    add("Fasting", "Натощак", "Ayuno", "Jeûne", "روزہ رکھنا", "ناشتا نبودن")
    add("Followed by a short rest.", "Затем короткий отдых.", "Seguido de un breve descanso.", "Suivi d’un court repos.", "پھر تھوڑا آرام۔", "سپس استراحت کوتاه.")
    add("For selected tumors after tumor board review", "Для отдельных опухолей после онкоконсилиума", "Para tumores seleccionados tras el comité de tumores", "Pour certaines tumeurs après la réunion de concertation", "ٹیومر بورڈ کے جائزے کے بعد منتخب ٹیومر کے لیے", "برای تومورهای منتخب پس از بررسی بورد تومور")
    add("For some thyroid conditions", "При некоторых болезнях щитовидной железы", "Para algunas afecciones tiroideas", "Pour certaines affections thyroïdiennes", "تھائرائیڈ کی کچھ حالتوں کے لیے", "برای برخی وضعیت‌های تیروئید")
    add("Gamma camera & SPECT/CT", "Гамма-камера и SPECT/CT", "Gammacámara y SPECT/CT", "Gamma-caméra et SPECT/CT", "گاما کیمرہ اور SPECT/CT", "دوربین گاما و SPECT/CT")
    add("Imaging", "Визуализация", "Imagen", "Imagerie", "امیجنگ", "تصویربرداری")
    add("In selected neurological cases", "В отдельных неврологических случаях", "En casos neurológicos seleccionados", "Dans des cas neurologiques sélectionnés", "منتخب اعصابی کیسوں میں", "در موارد عصبی منتخب")
    add("Injection", "Введение", "Inyección", "Injection", "انجیکشن", "تزریق")
    add("Is the radiation in PET/CT safe?", "Безопасно ли облучение при PET/CT?", "¿Es segura la radiación del PET/CT?", "Le rayonnement de la TEP/TDM est-il sûr ?", "کیا PET/CT کی تابکاری محفوظ ہے؟", "آیا پرتو PET/CT ایمن است؟")
    add("Myocardial perfusion", "Перфузия миокарда", "Perfusión miocárdica", "Perfusion myocardique", "دل کے پٹھے کی خون رسانی", "پرفیوژن میوکارد")
    add("Radioactive iodine", "Радиоактивный йод", "Yodo radiactivo", "Iode radioactif", "تابکار آیوڈین", "ید پرتوزا")
    add("Radionuclide", "Радионуклид", "Radionúclido", "Radionucléide", "ریڈیونیوکلائیڈ", "رادیونوکلئید")
    add("Radionuclide treatment", "Радионуклидное лечение", "Tratamiento con radionúclidos", "Traitement par radionucléides", "ریڈیونیوکلائیڈ علاج", "درمان رادیونوکلئید")
    add("Report", "Заключение", "Informe", "Compte rendu", "رپورٹ", "گزارش")
    same("SPECT/CT")
    add("Scan", "Сканирование", "Exploración", "Examen", "اسکین", "اسکن")
    add("Send reports for an imaging review", "Отправьте документы на разбор снимков", "Envíe informes para una revisión de imagen", "Envoyez les documents pour un examen d’imagerie", "امیجنگ جائزے کے لیے رپورٹس بھیجیں", "گزارش‌ها را برای بررسی تصویربرداری بفرستید")
    add("Sent to your treating physician.", "Направляется лечащему врачу.", "Se envía a su médico tratante.", "Envoyé à votre médecin traitant.", "آپ کے معالج کو بھیجا جاتا ہے۔", "برای پزشک معالج شما فرستاده می‌شود.")
    add("Targeted radionuclide therapy", "Таргетная радионуклидная терапия", "Terapia con radionúclidos dirigida", "Thérapie radionucléidique ciblée", "ٹارگٹڈ ریڈیونیوکلائیڈ تھراپی", "درمان هدفمند رادیونوکلئید")
    add("The dose is planned for diagnosis, and the team explains simple precautions after the scan.", "Доза планируется для диагностики, и команда объясняет простые меры предосторожности после исследования.", "La dosis se planifica para el diagnóstico, y el equipo explica precauciones sencillas después del estudio.", "La dose est prévue pour le diagnostic, et l’équipe explique des précautions simples après l’examen.", "خوراک تشخیص کے لیے طے ہوتی ہے، اور ٹیم اسکین کے بعد سادہ احتیاطیں بتاتی ہے۔", "دوز برای تشخیص برنامه‌ریزی می‌شود و تیم پس از اسکن احتیاط‌های ساده را توضیح می‌دهد.")
    add("Usually for some hours before.", "Обычно за несколько часов.", "Habitualmente durante algunas horas antes.", "En général pendant quelques heures avant.", "عام طور پر چند گھنٹے پہلے۔", "معمولاً چند ساعت پیش از آن.")
    add("Usually under an hour.", "Обычно меньше часа.", "Habitualmente menos de una hora.", "En général moins d’une heure.", "عام طور پر ایک گھنٹے سے کم۔", "معمولاً کمتر از یک ساعت.")
    add("Yes, bring the images in DICOM format.", "Да, привезите изображения в формате DICOM.", "Sí, traiga las imágenes en formato DICOM.", "Oui, apportez les images au format DICOM.", "جی ہاں، تصاویر DICOM فارمیٹ میں لائیں۔", "بله، تصویرها را در قالب DICOM بیاورید.")
    add("gamma camera", "гамма-камера", "gammacámara", "gamma-caméra", "گاما کیمرہ", "دوربین گاما")
    add("molecular imaging", "молекулярная визуализация", "imagen molecular", "imagerie moléculaire", "مالیکیولر امیجنگ", "تصویربرداری مولکولی")
    add("selected treatments", "отдельные методы лечения", "tratamientos seleccionados", "traitements sélectionnés", "منتخب علاج", "درمان‌های منتخب")
    add("Nuclear medicine in Istanbul | Biruni Bridge", "Ядерная медицина в Стамбуле | Biruni Bridge", "Medicina nuclear en Estambul | Biruni Bridge", "Médecine nucléaire à Istanbul | Biruni Bridge", "استنبول میں نیوکلیئر میڈیسن | Biruni Bridge", "پزشکی هسته‌ای در استانبول | Biruni Bridge")

    # Organ transplant
    add("Adjusting and monitoring after transplant.", "Коррекция и наблюдение после трансплантации.", "Ajuste y seguimiento después del trasplante.", "Ajustement et surveillance après la greffe.", "ٹرانسپلانٹ کے بعد ایڈجسٹمنٹ اور نگرانی۔", "تنظیم و پایش پس از پیوند.")
    add("After evaluation and approvals are complete.", "После того как обследование и согласования завершены.", "Cuando la valoración y las aprobaciones están completas.", "Une fois l’évaluation et les autorisations terminées.", "جب جائزہ اور منظوری مکمل ہو جائیں۔", "پس از آنکه ارزیابی و تأییدیه‌ها کامل شد.")
    add("All related physicians in the directory (5)", "Все связанные врачи в справочнике (5)", "Todos los médicos relacionados en el directorio (5)", "Tous les médecins concernés dans l’annuaire (5)", "ڈائریکٹری میں تمام متعلقہ معالج (5)", "همهٔ پزشکان مرتبط در فهرست (۵)")
    add("Compatibility and safety for both.", "Совместимость и безопасность для обоих.", "Compatibilidad y seguridad para ambos.", "Compatibilité et sécurité pour les deux.", "دونوں کے لیے مطابقت اور حفاظت۔", "سازگاری و ایمنی برای هر دو.")
    add("Does the donor travel with me?", "Донор едет вместе со мной?", "¿El donante viaja conmigo?", "Le donneur voyage-t-il avec moi ?", "کیا عطیہ دہندہ میرے ساتھ سفر کرتا ہے؟", "آیا دهنده با من سفر می‌کند؟")
    add("Donation rules (important)", "Правила донорства (важно)", "Normas de donación (importante)", "Règles du don (important)", "عطیہ کے قواعد (اہم)", "قاعده‌های اهدا (مهم)")
    add("Ethics committee", "Этический комитет", "Comité de ética", "Comité d’éthique", "اخلاقیات کمیٹی", "کمیتهٔ اخلاق")
    add("Exact document list for each country", "Точный список документов для каждой страны", "Lista exacta de documentos para cada país", "Liste exacte des documents pour chaque pays", "ہر ملک کے لیے دستاویزات کی درست فہرست", "فهرست دقیق مدارک برای هر کشور")
    add("Full tests for both.", "Полное обследование обоих.", "Pruebas completas para ambos.", "Examens complets pour les deux.", "دونوں کے مکمل ٹیسٹ۔", "آزمایش کامل برای هر دو.")
    add("Kidney & liver", "Почка и печень", "Riñón e hígado", "Rein et foie", "گردہ اور جگر", "کلیه و کبد")
    add("Living-donor transplant", "Трансплантация от живого донора", "Trasplante de donante vivo", "Greffe à partir d’un donneur vivant", "زندہ عطیہ دہندہ کا ٹرانسپلانٹ", "پیوند از دهندهٔ زنده")
    add("Near the hospital, then with your doctor.", "Рядом с больницей, затем у вашего врача.", "Cerca del hospital y luego con su médico.", "Près de l’hôpital, puis avec votre médecin.", "ہسپتال کے قریب، پھر آپ کے ڈاکٹر کے ساتھ۔", "نزدیک بیمارستان، سپس با پزشک شما.")
    add("Only once the hospital confirms their source and period.", "Только после того, как больница подтвердит источник и период.", "Solo cuando el hospital confirme su fuente y el periodo.", "Seulement une fois que l’hôpital en confirme la source et la période.", "صرف اس وقت جب ہسپتال ان کا ماخذ اور مدت تصدیق کرے۔", "فقط وقتی بیمارستان منبع و دورهٔ آن‌ها را تأیید کند.")
    add(
        "Organ trade is prohibited by law. We require official documents proving the donor–recipient relationship; unrelated-donor cases need ethics-committee approval.",
        "Торговля органами запрещена законом. Мы требуем официальные документы, подтверждающие родство донора и реципиента; случаи неродственного донора нуждаются в одобрении этического комитета.",
        "El comercio de órganos está prohibido por ley. Exigimos documentos oficiales que prueben la relación donante–receptor; los casos de donante no emparentado necesitan la aprobación del comité de ética.",
        "Le commerce d’organes est interdit par la loi. Nous exigeons des documents officiels prouvant le lien donneur–receveur ; les cas de donneur non apparenté nécessitent l’approbation du comité d’éthique.",
        "اعضا کی تجارت قانوناً ممنوع ہے۔ ہم عطیہ دہندہ اور وصول کنندہ کے رشتے کے سرکاری دستاویزات مانگتے ہیں؛ غیر متعلق عطیہ دہندہ کے کیس کو اخلاقیات کمیٹی کی منظوری چاہیے۔",
        "تجارت عضو به حکم قانون ممنوع است. مدارک رسمی دال بر رابطهٔ دهنده و گیرنده را می‌خواهیم؛ پروندهٔ دهندهٔ غیرخویشاوند به تأیید کمیتهٔ اخلاق نیاز دارد.",
    )
    add("Patient and potential donor files.", "Документы пациента и возможного донора.", "Expedientes del paciente y del posible donante.", "Dossiers du patient et du donneur potentiel.", "مریض اور ممکنہ عطیہ دہندہ کی فائلیں۔", "پروندهٔ بیمار و دهندهٔ احتمالی.")
    add("Proof of relationship and committee approval where needed.", "Подтверждение родства и, где нужно, одобрение комитета.", "Prueba del parentesco y aprobación del comité cuando haga falta.", "Preuve du lien et approbation du comité lorsque c’est nécessaire.", "رشتے کا ثبوت اور جہاں ضرورت ہو کمیٹی کی منظوری۔", "اثبات رابطه و تأیید کمیته جایی که لازم است.")
    add("Send patient and donor files", "Отправьте документы пациента и донора", "Envíe los expedientes del paciente y del donante", "Envoyez les dossiers du patient et du donneur", "مریض اور عطیہ دہندہ کی فائلیں بھیجیں", "پروندهٔ بیمار و دهنده را بفرستید")
    add("Transplant steps", "Этапы трансплантации", "Pasos del trasplante", "Étapes de la greffe", "ٹرانسپلانٹ کے مراحل", "گام‌های پیوند")
    add(
        "Usually a relative who proves the relationship with official documents, after a medical assessment that ensures their safety.",
        "Обычно родственник, который подтверждает родство официальными документами, после медицинского обследования, которое подтверждает его безопасность.",
        "Por lo general un familiar que prueba el parentesco con documentos oficiales, tras una valoración médica que garantiza su seguridad.",
        "En général un parent qui prouve le lien par des documents officiels, après une évaluation médicale qui assure sa sécurité.",
        "عام طور پر ایک رشتہ دار جو سرکاری دستاویزات سے رشتہ ثابت کرے، اس طبی جائزے کے بعد جو اس کی حفاظت یقینی بنائے۔",
        "معمولاً خویشاوندی که رابطه را با مدارک رسمی ثابت کند، پس از ارزیابی پزشکی که ایمنی او را اطمینان دهد.",
    )
    add("Visas for both, stay and follow-up.", "Визы для обоих, пребывание и наблюдение.", "Visados para ambos, estancia y seguimiento.", "Visas pour les deux, séjour et suivi.", "دونوں کے ویزے، قیام اور فالو اپ۔", "ویزا برای هر دو، اقامت و پیگیری.")
    add(
        "We do not publish success rates until the hospital confirms their source and period.",
        "Показатели результата мы не публикуем, пока больница не подтвердит их источник и период.",
        "No publicamos tasas de resultado hasta que el hospital confirme su fuente y el periodo.",
        "Nous ne publions pas de taux de résultat tant que l’hôpital n’en a pas confirmé la source et la période.",
        "ہم نتائج کی شرح اس وقت تک شائع نہیں کرتے جب تک ہسپتال ان کا ماخذ اور مدت تصدیق نہ کرے۔",
        "نرخ نتیجه را منتشر نمی‌کنیم تا بیمارستان منبع و دورهٔ آن را تأیید کند.",
    )
    add("What we provide", "Что мы обеспечиваем", "Qué ofrecemos", "Ce que nous assurons", "ہم کیا فراہم کرتے ہیں", "آنچه فراهم می‌کنیم")
    add("Who can be a donor?", "Кто может быть донором?", "¿Quién puede ser donante?", "Qui peut être donneur ?", "عطیہ دہندہ کون بن سکتا ہے؟", "چه کسی می‌تواند دهنده باشد؟")
    add("Yes. We arrange visas and accommodation for both of you.", "Да. Мы организуем визы и проживание для вас обоих.", "Sí. Organizamos visados y alojamiento para ambos.", "Oui. Nous organisons les visas et l’hébergement pour vous deux.", "جی ہاں۔ ہم دونوں کے ویزے اور رہائش کا بندوبست کرتے ہیں۔", "بله. ویزا و اقامت را برای هر دوی شما ترتیب می‌دهیم.")
    add(
        "differs for recipient and donor depending on transplant type and recovery.",
        "различается для реципиента и донора в зависимости от типа трансплантации и восстановления.",
        "difiere para el receptor y el donante según el tipo de trasplante y la recuperación.",
        "diffère pour le receveur et le donneur selon le type de greffe et la récupération.",
        "وصول کنندہ اور عطیہ دہندہ کے لیے ٹرانسپلانٹ کی قسم اور صحت یابی کے مطابق مختلف ہے۔",
        "برای گیرنده و دهنده بسته به نوع پیوند و بهبود فرق می‌کند.",
    )
    add("for donor approvals", "для согласования донора", "para las aprobaciones del donante", "pour les autorisations du donneur", "عطیہ دہندہ کی منظوری کے لیے", "برای تأیید دهنده")
    add("recipients", "реципиенты", "receptores", "receveurs", "وصول کنندگان", "گیرنده‌ها")
    add("transplant programs", "программы трансплантации", "programas de trasplante", "programmes de greffe", "ٹرانسپلانٹ پروگرام", "برنامه‌های پیوند")
    add("Organ transplant in Istanbul | Biruni Bridge", "Трансплантация органов в Стамбуле | Biruni Bridge", "Trasplante de órganos en Estambul | Biruni Bridge", "Greffe d’organes à Istanbul | Biruni Bridge", "استنبول میں اعضا کا ٹرانسپلانٹ | Biruni Bridge", "پیوند عضو در استانبول | Biruni Bridge")

    # Orthopedics
    add(
        f"Assisted walking usually starts early, depending on your condition and the team{A}s instructions.",
        "Ходьба с опорой обычно начинается рано и зависит от состояния и указаний команды.",
        "La marcha asistida suele empezar pronto, según su estado y las indicaciones del equipo.",
        "La marche aidée commence en général tôt, selon votre état et les consignes de l’équipe.",
        "سہارے کے ساتھ چلنا عام طور پر جلد شروع ہوتا ہے، آپ کی حالت اور ٹیم کی ہدایات کے مطابق۔",
        "راه رفتن با کمک معمولاً زود شروع می‌شود، بسته به وضعیت شما و دستور تیم.",
    )
    add("Disc herniation, stenosis and deformity", "Грыжа диска, стеноз и деформация", "Hernia discal, estenosis y deformidad", "Hernie discale, sténose et déformation", "ڈسک ہرنی، تنگی اور بگاڑ", "فتق دیسک، تنگی و بدشکلی")
    add("Do I need a companion?", "Нужен ли сопровождающий?", "¿Necesito un acompañante?", "Ai-je besoin d’un accompagnant ?", "کیا مجھے ساتھی کی ضرورت ہے؟", "آیا به همراه نیاز دارم؟")
    add("Exam and pre-op preparation.", "Осмотр и подготовка к операции.", "Exploración y preparación preoperatoria.", "Examen et préparation avant l’opération.", "معائنہ اور آپریشن سے پہلے کی تیاری۔", "معاینه و آمادگی پیش از عمل.")
    add("Is robotic surgery right for me?", "Подходит ли мне роботическая операция?", "¿La cirugía robótica es adecuada para mí?", "La chirurgie robotique me convient-elle ?", "کیا روبوٹک سرجری میرے لیے درست ہے؟", "آیا جراحی رباتیک برای من مناسب است؟")
    add("It is recommended for the first days.", "Это рекомендуют на первые дни.", "Se recomienda los primeros días.", "C’est recommandé les premiers jours.", "پہلے دنوں کے لیے یہ مشورہ دیا جاتا ہے۔", "برای روزهای نخست توصیه می‌شود.")
    add("Joint replacement", "Эндопротезирование сустава", "Prótesis articular", "Prothèse articulaire", "جوڑ کی تبدیلی", "تعویض مفصل")
    add("Joint replacement journey", "Путь эндопротезирования", "Recorrido de la prótesis articular", "Parcours de la prothèse articulaire", "جوڑ کی تبدیلی کا سفر", "مسیر تعویض مفصل")
    add("Knee and hip, robot-assisted where suitable", "Колено и тазобедренный сустав, с роботом, где это подходит", "Rodilla y cadera, asistida por robot cuando es adecuada", "Genou et hanche, assistée par robot lorsque c’est adapté", "گھٹنا اور کولہا، جہاں موزوں ہو روبوٹ کی مدد سے", "زانو و لگن، با کمک ربات جایی که مناسب است")
    add("Ligaments and cartilage by arthroscopy.", "Связки и хрящ артроскопически.", "Ligamentos y cartílago por artroscopia.", "Ligaments et cartilage par arthroscopie.", "آرتھروسکوپی سے رباط اور کارٹیلیج۔", "رباط و غضروف با آرتروسکوپی.")
    add(
        "Orthopedic surgeons assess your X-rays and MRI before you travel and explain whether surgery is needed or another treatment is enough. For knee and hip replacement, a robotic system may be used to support precise planning and execution.",
        "Ортопеды смотрят рентген и МРТ до поездки и объясняют, нужна ли операция или достаточно другого лечения. При эндопротезировании колена и тазобедренного сустава роботическая система может использоваться для точного планирования и выполнения.",
        "Los cirujanos ortopédicos valoran sus radiografías y su resonancia antes del viaje y explican si hace falta cirugía u otro tratamiento basta. En la prótesis de rodilla y cadera puede usarse un sistema robótico para apoyar una planificación y una ejecución precisas.",
        "Les chirurgiens orthopédistes examinent vos radiographies et votre IRM avant le voyage et expliquent si la chirurgie est nécessaire ou si un autre traitement suffit. Pour la prothèse de genou et de hanche, un système robotique peut servir à une planification et une réalisation précises.",
        "آرتھوپیڈک سرجن سفر سے پہلے ایکس رے اور MRI دیکھتے ہیں اور بتاتے ہیں کہ سرجری ضروری ہے یا دوسرا علاج کافی ہے۔ گھٹنے اور کولہے کی تبدیلی میں درست منصوبہ بندی اور انجام کے لیے روبوٹک نظام استعمال ہو سکتا ہے۔",
        "جراحان ارتوپدی پیش از سفر پرتونگاری و MRI را می‌بینند و توضیح می‌دهند جراحی لازم است یا درمان دیگر کافی است. برای تعویض زانو و لگن ممکن است سامانهٔ رباتیک برای برنامه‌ریزی و اجرای دقیق به کار رود.",
    )
    add("Orthopedics and robot-assisted surgery", "Ортопедия и робот-ассистированная хирургия", "Ortopedia y cirugía asistida por robot", "Orthopédie et chirurgie assistée par robot", "آرتھوپیڈکس اور روبوٹ کی مدد سے سرجری", "ارتوپدی و جراحی با کمک ربات")
    add("Recent X-rays and MRI if any.", "Недавние рентгенограммы и МРТ, если есть.", "Radiografías recientes y resonancia si las hay.", "Radiographies récentes et IRM s’il y en a.", "حالیہ ایکس رے اور MRI اگر ہوں۔", "پرتونگاری اخیر و MRI اگر باشد.")
    add("Robot-assisted where suitable.", "С роботом, где это подходит.", "Asistida por robot cuando es adecuada.", "Assistée par robot lorsque c’est adapté.", "جہاں موزوں ہو روبوٹ کی مدد سے۔", "با کمک ربات جایی که مناسب است.")
    add("Robot-assisted surgery", "Робот-ассистированная хирургия", "Cirugía asistida por robot", "Chirurgie assistée par robot", "روبوٹ کی مدد سے سرجری", "جراحی با کمک ربات")
    add("Send your X-rays and reports", "Отправьте рентген и заключения", "Envíe sus radiografías e informes", "Envoyez vos radiographies et comptes rendus", "ایکس رے اور رپورٹس بھیجیں", "پرتونگاری و گزارش‌ها را بفرستید")
    add("Sports injuries", "Спортивные травмы", "Lesiones deportivas", "Blessures sportives", "کھیلوں کی چوٹیں", "آسیب ورزشی")
    add("Starts early after surgery.", "Начинается рано после операции.", "Empieza pronto después de la cirugía.", "Commence tôt après la chirurgie.", "سرجری کے بعد جلد شروع ہوتی ہے۔", "زود پس از جراحی شروع می‌شود.")
    add("The surgeon decides based on the joint and imaging.", "Хирург решает по суставу и снимкам.", "El cirujano decide según la articulación y la imagen.", "Le chirurgien décide selon l’articulation et l’imagerie.", "سرجن جوڑ اور امیجنگ کی بنیاد پر فیصلہ کرتا ہے۔", "جراح بر اساس مفصل و تصویربرداری تصمیم می‌گیرد.")
    add("Trauma & fractures", "Травмы и переломы", "Traumatismos y fracturas", "Traumatismes et fractures", "چوٹ اور فریکچر", "تروما و شکستگی")
    add("When will I walk after knee replacement?", "Когда я смогу ходить после эндопротезирования колена?", "¿Cuándo caminaré después de una prótesis de rodilla?", "Quand marcherai-je après une prothèse de genou ?", "گھٹنے کی تبدیلی کے بعد میں کب چل سکوں گا/گی؟", "پس از تعویض زانو چه وقت راه می‌روم؟")
    add("With a physiotherapy plan for home.", "С планом физиотерапии для дома.", "Con un plan de fisioterapia para casa.", "Avec un plan de kinésithérapie pour la maison.", "گھر کے لیے فزیوتھراپی کے منصوبے کے ساتھ۔", "با برنامهٔ فیزیوتراپی برای خانه.")
    add(
        "depends on the surgery and rehabilitation; the surgeon decides when you can fly.",
        "зависит от операции и реабилитации; хирург решает, когда можно лететь.",
        "depende de la cirugía y la rehabilitación; el cirujano decide cuándo puede volar.",
        "dépend de la chirurgie et de la rééducation ; le chirurgien décide quand vous pouvez prendre l’avion.",
        "سرجری اور بحالی پر منحصر ہے؛ سرجن فیصلہ کرتا ہے کہ آپ کب پرواز کر سکتے ہیں۔",
        "به جراحی و بازتوانی بستگی دارد؛ جراح تصمیم می‌گیرد چه وقت می‌توانید پرواز کنید.",
    )
    add("for joint replacement", "для эндопротезирования", "para la prótesis articular", "pour la prothèse articulaire", "جوڑ کی تبدیلی کے لیے", "برای تعویض مفصل")
    add("physiotherapy after surgery", "физиотерапия после операции", "fisioterapia después de la cirugía", "kinésithérapie après la chirurgie", "سرجری کے بعد فزیوتھراپی", "فیزیوتراپی پس از جراحی")
    add("Orthopedics & robot-assisted surgery in Istanbul | Biruni Bridge", "Ортопедия и робот-ассистированная хирургия в Стамбуле | Biruni Bridge", "Ortopedia y cirugía asistida por robot en Estambul | Biruni Bridge", "Orthopédie et chirurgie assistée par robot à Istanbul | Biruni Bridge", "استنبول میں آرتھوپیڈکس اور روبوٹ کی مدد سے سرجری | Biruni Bridge", "ارتوپدی و جراحی با کمک ربات در استانبول | Biruni Bridge")

    # Pediatric hematology-oncology
    add("A parent stays with the child", "Родитель остаётся с ребёнком", "Un padre o una madre se queda con el niño", "Un parent reste avec l’enfant", "ایک والدین بچے کے ساتھ رہتے ہیں", "یک والد کنار کودک می‌ماند")
    add("Bleeding disorders", "Нарушения свёртывания", "Trastornos hemorrágicos", "Troubles de la coagulation", "خون بہنے کے عوارض", "اختلال خونریزی")
    add("Blood disorders", "Болезни крови", "Trastornos de la sangre", "Troubles du sang", "خون کے عوارض", "اختلال‌های خون")
    add("Can parents stay with the child?", "Могут ли родители оставаться с ребёнком?", "¿Los padres pueden quedarse con el niño?", "Les parents peuvent-ils rester avec l’enfant ?", "کیا والدین بچے کے ساتھ رہ سکتے ہیں؟", "آیا والدین می‌توانند کنار کودک بمانند؟")
    add("Childhood cancers", "Детские онкологические заболевания", "Cánceres infantiles", "Cancers de l’enfant", "بچپن کے کینسر", "سرطان‌های کودکی")
    add("Coordinator & interpreter", "Координатор и переводчик", "Coordinador e intérprete", "Coordinateur et interprète", "کوآرڈینیٹر اور ترجمان", "هماهنگ‌کننده و مترجم")
    add("Do you perform pediatric bone marrow transplants?", "Делаете ли вы детскую трансплантацию костного мозга?", "¿Realizan trasplantes de médula ósea pediátricos?", "Faites-vous des greffes de moelle osseuse pédiatriques ?", "کیا آپ بچوں کا بون میرو ٹرانسپلانٹ کرتے ہیں؟", "آیا پیوند مغز استخوان کودکان انجام می‌دهید؟")
    add("For child and parents", "Для ребёнка и родителей", "Para el niño y los padres", "Pour l’enfant et les parents", "بچے اور والدین کے لیے", "برای کودک و والدین")
    add("Immunodeficiency", "Иммунодефицит", "Inmunodeficiencia", "Déficit immunitaire", "امیونو ڈیفیشنسی", "نقص ایمنی")
    add("Medical reports, biopsy or bone marrow report, recent tests and previous treatments.", "Медицинские заключения, биопсия или исследование костного мозга, недавние анализы и предыдущее лечение.", "Informes médicos, biopsia o informe de médula, pruebas recientes y tratamientos previos.", "Comptes rendus médicaux, biopsie ou compte rendu de moelle, examens récents et traitements antérieurs.", "میڈیکل رپورٹس، بایوپسی یا بون میرو رپورٹ، حالیہ ٹیسٹ اور سابقہ علاج۔", "گزارش پزشکی، بیوپسی یا گزارش مغز استخوان، آزمایش اخیر و درمان‌های قبلی.")
    add("Pediatric BMT", "Детская трансплантация костного мозга", "TMO pediátrico", "Greffe de moelle pédiatrique", "بچوں کا بون میرو ٹرانسپلانٹ", "پیوند مغز استخوان کودکان")
    add(
        "Pediatric hematologist-oncologists work with pediatric surgery, child neurology, intensive care and the transplant team. We make sure the child and family understand every step, in their language.",
        "Детские гематологи-онкологи работают с детской хирургией, детской неврологией, реанимацией и командой трансплантации. Мы следим, чтобы ребёнок и семья понимали каждый шаг на своём языке.",
        "Los hematólogos-oncólogos pediátricos trabajan con cirugía pediátrica, neurología infantil, cuidados intensivos y el equipo de trasplante. Nos aseguramos de que el niño y la familia entiendan cada paso, en su idioma.",
        "Les hématologues-oncologues pédiatres travaillent avec la chirurgie pédiatrique, la neurologie de l’enfant, les soins intensifs et l’équipe de greffe. Nous veillons à ce que l’enfant et la famille comprennent chaque étape, dans leur langue.",
        "بچوں کے ہیماٹولوجسٹ آنکولوجسٹ بچوں کی سرجری، بچوں کی نیورولوجی، انتہائی نگہداشت اور ٹرانسپلانٹ ٹیم کے ساتھ کام کرتے ہیں۔ ہم یقینی بناتے ہیں کہ بچہ اور خاندان ہر قدم اپنی زبان میں سمجھیں۔",
        "متخصصان خون و انکولوژی کودکان با جراحی کودکان، نورولوژی کودک، مراقبت ویژه و تیم پیوند کار می‌کنند. مطمئن می‌شویم کودک و خانواده هر گام را به زبان خود بفهمند.",
    )
    add("Pediatric hematology and oncology", "Детская гематология и онкология", "Hematología y oncología pediátricas", "Hématologie et oncologie pédiatriques", "بچوں کی ہیماٹولوجی اور آنکولوجی", "خون‌شناسی و انکولوژی کودکان")
    add("Psychological support", "Психологическая поддержка", "Apoyo psicológico", "Soutien psychologique", "نفسیاتی مدد", "حمایت روان‌شناختی")
    add("Schooling during treatment", "Обучение во время лечения", "Escolarización durante el tratamiento", "Scolarité pendant le traitement", "علاج کے دوران تعلیم", "تحصیل در طول درمان")
    add(f"Send your child{A}s reports", "Отправьте документы ребёнка", "Envíe los informes de su hijo", "Envoyez les documents de votre enfant", "بچے کی رپورٹس بھیجیں", "گزارش‌های کودک را بفرستید")
    add("Sickle cell disease", "Серповидноклеточная анемия", "Drepanocitosis", "Drépanocytose", "سکل سیل بیماری", "بیماری سلول داسی")
    add("Solid tumors", "Солидные опухоли", "Tumores sólidos", "Tumeurs solides", "ٹھوس ٹیومر", "تومور توپر")
    add("Support for child and family", "Поддержка ребёнка и семьи", "Apoyo al niño y a la familia", "Soutien à l’enfant et à la famille", "بچے اور خاندان کی مدد", "حمایت از کودک و خانواده")
    add("Thalassemia", "Талассемия", "Talasemia", "Thalassémie", "تھیلیسیمیا", "تالاسمی")
    add("To explain every procedure to the family.", "Чтобы объяснить семье каждую процедуру.", "Para explicar cada procedimiento a la familia.", "Pour expliquer chaque geste à la famille.", "خاندان کو ہر طریقہ کار سمجھانے کے لیے۔", "برای توضیح هر اقدام به خانواده.")
    add("Travelling with a sick child", "Поездка с больным ребёнком", "Viajar con un niño enfermo", "Voyager avec un enfant malade", "بیمار بچے کے ساتھ سفر", "سفر با کودک بیمار")
    add("Under hospital policy.", "По правилам больницы.", "Según la política del hospital.", "Selon la politique de l’hôpital.", "ہسپتال کی پالیسی کے تحت۔", "طبق سیاست بیمارستان.")
    add(
        "We review the file first and tell you honestly whether travelling is safe and useful, or whether continuing treatment at home is better.",
        "Сначала мы читаем документы и честно говорим, безопасна и полезна ли поездка или лучше продолжить лечение дома.",
        "Primero revisamos el expediente y le decimos con claridad si viajar es seguro y útil, o si es mejor continuar el tratamiento en casa.",
        "Nous examinons d’abord le dossier et vous disons clairement si le voyage est sûr et utile, ou s’il vaut mieux poursuivre le traitement à la maison.",
        "ہم پہلے فائل دیکھتے ہیں اور ایمانداری سے بتاتے ہیں کہ سفر محفوظ اور مفید ہے یا گھر علاج جاری رکھنا بہتر ہے۔",
        "ابتدا پرونده را می‌خوانیم و روشن می‌گوییم سفر ایمن و مفید است یا ادامهٔ درمان در خانه بهتر است.",
    )
    add("Which documents are needed?", "Какие документы нужны?", "¿Qué documentos hacen falta?", "Quels documents sont nécessaires ?", "کون سی دستاویزات درکار ہیں؟", "کدام مدارک لازم است؟")
    add("Yes, at least one parent, under hospital policy.", "Да, как минимум один родитель, по правилам больницы.", "Sí, al menos un padre o una madre, según la política del hospital.", "Oui, au moins un parent, selon la politique de l’hôpital.", "جی ہاں، کم از کم ایک والدین، ہسپتال کی پالیسی کے تحت۔", "بله، دست‌کم یک والد، طبق سیاست بیمارستان.")
    add("Yes, in the pediatric bone marrow transplant unit.", "Да, в детском отделении трансплантации костного мозга.", "Sí, en la unidad pediátrica de trasplante de médula ósea.", "Oui, dans l’unité pédiatrique de greffe de moelle osseuse.", "جی ہاں، بچوں کے بون میرو ٹرانسپلانٹ یونٹ میں۔", "بله، در بخش پیوند مغز استخوان کودکان.")
    add("neonatal incubators", "кувезы для новорождённых", "incubadoras neonatales", "incubateurs néonatals", "نوزائیدہ انکیوبیٹر", "انکوباتور نوزاد")
    add("pediatric isolation rooms", "детские изоляторы", "habitaciones de aislamiento pediátricas", "chambres d’isolement pédiatriques", "بچوں کے آئسولیشن کمرے", "اتاق ایزولهٔ کودکان")
    add("under one roof", "под одной крышей", "bajo un mismo techo", "sous le même toit", "ایک ہی چھت کے نیچے", "زیر یک سقف")
    add("Pediatric hematology & oncology in Istanbul | Biruni Bridge", "Детская гематология и онкология в Стамбуле | Biruni Bridge", "Hematología y oncología pediátricas en Estambul | Biruni Bridge", "Hématologie et oncologie pédiatriques à Istanbul | Biruni Bridge", "استنبول میں بچوں کی ہیماٹولوجی اور آنکولوجی | Biruni Bridge", "خون‌شناسی و انکولوژی کودکان در استانبول | Biruni Bridge")

    # Radiation oncology
    add("About length of stay:", "О длительности пребывания:", "Sobre la duración de la estancia:", "À propos de la durée du séjour :", "قیام کی مدت کے بارے میں:", "دربارهٔ مدت اقامت:")
    add("CT simulation", "КТ-симуляция", "Simulación por TC", "Simulation TDM", "CT سمیولیشن", "شبیه‌سازی CT")
    add("How treatment works", "Как проходит лечение", "Cómo funciona el tratamiento", "Comment se déroule le traitement", "علاج کیسے ہوتا ہے", "درمان چگونه پیش می‌رود")
    add("Linear accelerator", "Линейный ускоритель", "Acelerador lineal", "Accélérateur linéaire", "لینیئر ایکسلریٹر", "شتاب‌دهندهٔ خطی")
    add(
        "Radiotherapy uses high-energy beams to target the tumor while sparing healthy tissue as much as possible. It may be used alone or with surgery and drug treatment, as decided by the tumor board.",
        "Лучевая терапия использует пучки высокой энергии, чтобы воздействовать на опухоль и по возможности щадить здоровые ткани. Её применяют отдельно или вместе с операцией и лекарственным лечением, как решит онкоконсилиум.",
        "La radioterapia usa haces de alta energía para dirigirse al tumor y preservar el tejido sano en la medida de lo posible. Puede usarse sola o con cirugía y tratamiento farmacológico, según decida el comité de tumores.",
        "La radiothérapie utilise des faisceaux de haute énergie pour cibler la tumeur tout en épargnant autant que possible le tissu sain. Elle peut être utilisée seule ou avec la chirurgie et un traitement médicamenteux, selon la décision de la réunion de concertation.",
        "ریڈیوتھراپی زیادہ توانائی کی شعاعوں سے ٹیومر کو نشانہ بناتی ہے اور صحت مند بافت کو جتنا ممکن ہو بچاتی ہے۔ یہ اکیلے یا سرجری اور دوائی کے علاج کے ساتھ استعمال ہو سکتی ہے، جیسا ٹیومر بورڈ فیصلہ کرے۔",
        "پرتودرمانی با پرتوهای پرانرژی تومور را هدف می‌گیرد و تا حد ممکن بافت سالم را حفظ می‌کند. ممکن است تنها یا همراه جراحی و درمان دارویی به کار رود، آن‌گونه که بورد تومور تصمیم بگیرد.",
    )
    add("Send reports for a radiotherapy review", "Отправьте документы на разбор лучевой терапии", "Envíe informes para una revisión de radioterapia", "Envoyez les documents pour un examen de radiothérapie", "ریڈیوتھراپی جائزے کے لیے رپورٹس بھیجیں", "گزارش‌ها را برای بررسی پرتودرمانی بفرستید")
    add("for precise planning", "для точного планирования", "para una planificación precisa", "pour une planification précise", "درست منصوبہ بندی کے لیے", "برای برنامه‌ریزی دقیق")
    add("intensity-modulated techniques", "методики с модуляцией интенсивности", "técnicas de intensidad modulada", "techniques à modulation d’intensité", "شدت کی تبدیلی والی تکنیک", "روش‌های با شدت تعدیل‌شده")
    add(
        "radiotherapy often runs for weeks; we discuss whether completing it at home or in Istanbul suits you better.",
        "лучевая терапия часто длится неделями; мы обсуждаем, что вам больше подходит — закончить её дома или в Стамбуле.",
        "la radioterapia suele durar semanas; comentamos si le conviene más completarla en casa o en Estambul.",
        "la radiothérapie dure souvent des semaines ; nous discutons s’il vous convient mieux de la terminer à la maison ou à Istanbul.",
        "ریڈیوتھراپی اکثر ہفتوں چلتی ہے؛ ہم بات کرتے ہیں کہ اسے گھر مکمل کرنا بہتر ہے یا استنبول میں۔",
        "پرتودرمانی اغلب هفته‌ها طول می‌کشد؛ گفتگو می‌کنیم تکمیل آن در خانه مناسب‌تر است یا در استانبول.",
    )
    add("Radiation oncology in Istanbul | Biruni Bridge", "Лучевая терапия в Стамбуле | Biruni Bridge", "Oncología radioterápica en Estambul | Biruni Bridge", "Oncologie radiothérapique à Istanbul | Biruni Bridge", "استنبول میں ریڈی ایشن آنکولوجی | Biruni Bridge", "انکولوژی پرتویی در استانبول | Biruni Bridge")

    # Surgical oncology
    add("Areas of cancer surgery", "Области онкохирургии", "Áreas de cirugía oncológica", "Domaines de la chirurgie du cancer", "کینسر سرجری کے شعبے", "حوزه‌های جراحی سرطان")
    add("Before and after surgery", "До и после операции", "Antes y después de la cirugía", "Avant et après la chirurgie", "سرجری سے پہلے اور بعد", "پیش و پس از جراحی")
    add("Send reports for a surgical review", "Отправьте документы на хирургический разбор", "Envíe informes para una revisión quirúrgica", "Envoyez les documents pour un examen chirurgical", "سرجیکل جائزے کے لیے رپورٹس بھیجیں", "گزارش‌ها را برای بررسی جراحی بفرستید")
    add(
        "The timing and type of surgery are decided by the tumor board: it may come before or after drug or radiation treatment. We review imaging and biopsy before anything is booked, to explain whether surgery is the right option at all.",
        "Срок и вид операции решает онкоконсилиум: она может быть до или после лекарственного или лучевого лечения. Снимки и биопсию мы смотрим до любой записи, чтобы объяснить, является ли операция подходящим вариантом вообще.",
        "El momento y el tipo de cirugía los decide el comité de tumores: puede ser antes o después del tratamiento farmacológico o de la radioterapia. Revisamos la imagen y la biopsia antes de reservar nada, para explicar si la cirugía es la opción adecuada.",
        "Le moment et le type de chirurgie sont décidés en réunion de concertation : elle peut avoir lieu avant ou après un traitement médicamenteux ou par rayons. Nous examinons l’imagerie et la biopsie avant toute réservation, pour expliquer si la chirurgie est la bonne option.",
        "سرجری کا وقت اور قسم ٹیومر بورڈ طے کرتا ہے: یہ دوا یا شعاعی علاج سے پہلے یا بعد ہو سکتی ہے۔ کچھ بک ہونے سے پہلے ہم امیجنگ اور بایوپسی دیکھتے ہیں، تاکہ بتائیں کہ سرجری درست اختیار ہے یا نہیں۔",
        "زمان و نوع جراحی را بورد تومور تعیین می‌کند: ممکن است پیش یا پس از درمان دارویی یا پرتو باشد. پیش از هر رزروی تصویربرداری و بیوپسی را می‌بینیم تا توضیح دهیم جراحی اصلاً گزینهٔ درست است یا نه.",
    )
    add("Surgical oncology in Istanbul | Biruni Bridge", "Хирургическая онкология в Стамбуле | Biruni Bridge", "Oncología quirúrgica en Estambul | Biruni Bridge", "Oncologie chirurgicale à Istanbul | Biruni Bridge", "استنبول میں سرجیکل آنکولوجی | Biruni Bridge", "انکولوژی جراحی در استانبول | Biruni Bridge")
