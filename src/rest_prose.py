"""Page prose. Facts follow the English pages."""

from __future__ import annotations

A = "\u2019"
LQ = "\u201c"
RQ = "\u201d"

PROSE_ROWS: list[tuple[str, str, str, str, str, str]] = []


def add(en: str, ru: str, es: str, fr: str, ur: str, fa: str) -> None:
    PROSE_ROWS.append((en, ru, es, fr, ur, fa))


# ----- about -----
add(
    "About Us | Biruni Bridge – Biruni University Hospital",
    "О нас | Biruni Bridge – больница Университета Бируни",
    "Quiénes somos | Biruni Bridge – Hospital Universitario Biruni",
    "Qui sommes-nous | Biruni Bridge – Hôpital universitaire Biruni",
    "ہمارے بارے میں | Biruni Bridge – Biruni یونیورسٹی ہسپتال",
    "دربارهٔ ما | بیرونی بریج – بیمارستان دانشگاه بیرونی",
)
add(
    "Biruni University Faculty of Medicine Hospital · since 2016",
    "Больница медицинского факультета Университета Бируни · с 2016 года",
    "Hospital de la Facultad de Medicina de la Universidad Biruni · desde 2016",
    "Hôpital de la Faculté de médecine de l’Université Biruni · depuis 2016",
    "Biruni یونیورسٹی فیکلٹی آف میڈیسن ہسپتال · 2016 سے",
    "بیمارستان دانشکدهٔ پزشکی دانشگاه بیرونی · از ۲۰۱۶",
)
add(
    "About us: a university hospital that stays with you, from home and back",
    "О нас: университетская больница, которая сопровождает вас от дома и обратно",
    "Quiénes somos: un hospital universitario que le acompaña desde su casa y de regreso",
    "Qui sommes-nous : un hôpital universitaire qui vous accompagne depuis chez vous et au retour",
    "ہمارے بارے میں: ایک یونیورسٹی ہسپتال جو گھر سے واپسی تک آپ کے ساتھ رہتا ہے",
    "دربارهٔ ما: بیمارستان دانشگاهی که از خانه تا بازگشت کنارتان است",
)
add(
    "Biruni Bridge is the international patient service of Biruni University Faculty of Medicine Hospital in Istanbul. We receive your inquiry, take your file to the right specialists, and organize your trip and follow-up.",
    "Biruni Bridge — служба для иностранных пациентов больницы медицинского факультета Университета Бируни в Стамбуле. Мы принимаем запрос, передаём документы нужным специалистам и организуем поездку и наблюдение.",
    "Biruni Bridge es el servicio de pacientes internacionales del Hospital de la Facultad de Medicina de la Universidad Biruni en Estambul. Recibimos su consulta, llevamos el expediente a los especialistas adecuados y organizamos el viaje y el seguimiento.",
    "Biruni Bridge est le service des patients internationaux de l’Hôpital de la Faculté de médecine de l’Université Biruni à Istanbul. Nous recevons votre demande, transmettons le dossier aux spécialistes concernés et organisons le voyage et le suivi.",
    "Biruni Bridge استنبول میں Biruni یونیورسٹی فیکلٹی آف میڈیسن ہسپتال کی بین الاقوامی مریض سروس ہے۔ ہم آپ کی درخواست لیتے ہیں، فائل درست ماہرین تک پہنچاتے ہیں، اور سفر و فالو اپ کا بندوبست کرتے ہیں۔",
    "بیرونی بریج خدمات بیماران بین‌المللی بیمارستان دانشکدهٔ پزشکی دانشگاه بیرونی در استانبول است. درخواست را می‌گیریم، پرونده را به متخصصان مناسب می‌رسانیم و سفر و پیگیری را هماهنگ می‌کنیم.",
)
add("Who we are", "Кто мы", "Quiénes somos", "Qui nous sommes", "ہم کون ہیں", "ما که هستیم")
add("A complete", "Больница", "Un hospital", "Un hôpital", "ایک مکمل", "بیمارستانی")
add("university hospital", "полного университетского профиля", "universitario de perfil completo", "universitaire de plein exercice", "یونیورسٹی ہسپتال", "دانشگاهی با بخش‌های کامل")
add(
    f"Biruni University Faculty of Medicine Hospital was founded in 2016 with a {LQ}university hospital{RQ} vision. It is a 12-storey complex on 80,000 m² with modern technology and smart-building infrastructure, staffed by academic physicians who combine patient care, teaching and research.",
    "Больница медицинского факультета Университета Бируни открыта в 2016 году с замыслом университетской больницы. Это 12-этажный комплекс площадью 80 000 м² с современным оборудованием и инфраструктурой «умного» здания; здесь работают преподаватели, которые совмещают лечение, обучение и исследования.",
    "El Hospital de la Facultad de Medicina de la Universidad Biruni se fundó en 2016 con la idea de hospital universitario. Es un complejo de 12 plantas y 80.000 m², con tecnología actual e infraestructura de edificio inteligente, y médicos docentes que unen la atención, la docencia y la investigación.",
    "L’Hôpital de la Faculté de médecine de l’Université Biruni a ouvert en 2016 avec l’idée d’un hôpital universitaire. C’est un ensemble de 12 étages sur 80 000 m², avec une technologie actuelle et une infrastructure de bâtiment intelligent, où des médecins enseignants associent soins, enseignement et recherche.",
    "Biruni یونیورسٹی فیکلٹی آف میڈیسن ہسپتال 2016 میں یونیورسٹی ہسپتال کے تصور کے ساتھ قائم ہوا۔ یہ 12 منزلہ، 80,000 مربع میٹر کا مجموعہ ہے، جدید ٹیکنالوجی اور سمارٹ عمارت کے ساتھ، جہاں تدریسی معالج مریض کی دیکھ بھال، تدریس اور تحقیق اکٹھے کرتے ہیں۔",
    "بیمارستان دانشکدهٔ پزشکی دانشگاه بیرونی در ۲۰۱۶ با ایدهٔ بیمارستان دانشگاهی بنا شد. مجموعه‌ای ۱۲ طبقه در ۸۰٬۰۰۰ مترمربع است، با فناوری روز و زیرساخت ساختمان هوشمند، و پزشکان هیئت علمی که درمان، آموزش و پژوهش را با هم انجام می‌دهند.",
)
add("A university hospital", "Университетская больница", "Un hospital universitario", "Un hôpital universitaire", "ایک یونیورسٹی ہسپتال", "بیمارستان دانشگاهی")
add("Evidence-based, multidisciplinary decisions.", "Решения на основе данных и мнения нескольких специальностей.", "Decisiones basadas en la evidencia y multidisciplinares.", "Décisions fondées sur les données et pluridisciplinaires.", "شواہد پر مبنی، کئی شعبوں کے فیصلے۔", "تصمیم‌های مبتنی بر شواهد و چندتخصصی.")
add("Specialized centers under one roof", "Профильные центры в одном комплексе", "Centros especializados bajo un mismo techo", "Des centres spécialisés sous un même toit", "ایک ہی چھت کے نیچے خصوصی مراکز", "مراکز تخصصی زیر یک سقف")
add(
    "Oncology, bone marrow and organ transplant, cardiology, IVF, children’s health, orthopedics and more.",
    "Онкология, трансплантация костного мозга и органов, кардиология, ЭКО, здоровье детей, ортопедия и другое.",
    "Oncología, trasplante de médula y de órganos, cardiología, FIV, salud infantil, ortopedia y más.",
    "Oncologie, greffe de moelle et d’organes, cardiologie, FIV, santé de l’enfant, orthopédie et d’autres domaines.",
    "آنکولوجی، بون میرو اور اعضا کی پیوند کاری، امراضِ قلب، آئی وی ایف، بچوں کی صحت، آرتھوپیڈکس اور مزید۔",
    "انکولوژی، پیوند مغز استخوان و اعضا، قلب، آی‌وی‌اف، سلامت کودک، ارتوپدی و موارد دیگر.",
)
add("An international team", "Международная команда", "Un equipo internacional", "Une équipe internationale", "بین الاقوامی ٹیم", "تیم بین‌المللی")
add(
    "Arabic, English, Russian, Spanish, German, French, Uzbek, Kazakh and more.",
    "Арабский, английский, русский, испанский, немецкий, французский, узбекский, казахский и другие.",
    "Árabe, inglés, ruso, español, alemán, francés, uzbeko, kazajo y otros.",
    "Arabe, anglais, russe, espagnol, allemand, français, ouzbek, kazakh et d’autres.",
    "عربی، انگریزی، روسی، ہسپانوی، جرمن، فرانسیسی، ازبک، قازق اور مزید۔",
    "عربی، انگلیسی، روسی، اسپانیایی، آلمانی، فرانسوی، ازبکی، قزاقی و زبان‌های دیگر.",
)
add("Modern technology", "Современное оборудование", "Tecnología actual", "Technologie actuelle", "جدید ٹیکنالوجی", "فناوری روز")
add(
    "3T MRI, low-dose CT, PET/CT, hybrid OR, robotic surgery, in-house genetics lab.",
    "МРТ 3 Тл, низкодозная КТ, ПЭТ/КТ, гибридная операционная, роботическая хирургия, собственная генетическая лаборатория.",
    "RM 3 T, TC de baja dosis, PET/TC, quirófano híbrido, cirugía robótica, laboratorio de genética propio.",
    "IRM 3 T, scanner faible dose, TEP/TDM, bloc hybride, chirurgie robotique, laboratoire de génétique sur place.",
    "3T ایم آر آئی، کم خوراک سی ٹی، PET/CT، ہائبرڈ آپریشن تھیٹر، روبوٹک سرجری، اپنی جینیات لیبارٹری۔",
    "ام‌آرآی ۳ تسلا، سی‌تی با دوز کم، PET/CT، اتاق عمل هیبرید، جراحی رباتیک، آزمایشگاه ژنتیک داخلی.",
)
add("The hospital in figures", "Больница в цифрах", "El hospital en cifras", "L’hôpital en chiffres", "ہسپتال اعداد میں", "بیمارستان در عدد")
add("Figures", "Цифры", "Cifras", "Chiffres", "اعداد", "عددها")
add("from hospital data", "по данным больницы", "según datos del hospital", "d’après les données de l’hôpital", "ہسپتال کے ڈیٹا سے", "از داده‌های بیمارستان")
add("beds", "коек", "camas", "lits", "بستر", "تخت")
add("ICU beds (neonatal, pediatric, adult)", "койки реанимации (новорождённые, дети, взрослые)", "camas de UCI (neonatal, pediátrica, de adultos)", "lits de réanimation (néonatale, pédiatrique, adulte)", "آئی سی یو بستر (نوزائیدہ، بچے، بالغ)", "تخت مراقبت ویژه (نوزاد، کودک، بزرگسال)")
add("operating rooms incl. hybrid", "операционных, включая гибридную", "quirófanos, incluido el híbrido", "salles d’opération, dont un bloc hybride", "آپریشن تھیٹر، ہائبرڈ سمیت", "اتاق عمل، از جمله هیبرید")
add("outpatient clinics", "амбулаторных кабинетов", "consultas externas", "consultations externes", "بیرونی کلینک", "درمانگاه سرپایی")
add("physicians and healthcare professionals", "врачей и медицинских сотрудников", "médicos y profesionales sanitarios", "médecins et soignants", "معالج اور طبی عملہ", "پزشک و کارکنان درمان")
add("surgical interventions a year", "хирургических вмешательств в год", "intervenciones quirúrgicas al año", "interventions chirurgicales par an", "سالانہ جراحی مداخلتیں", "مداخلهٔ جراحی در سال")
add("countries served", "стран, откуда приезжают пациенты", "países atendidos", "pays d’origine des patients", "ممالک جہاں سے مریض آتے ہیں", "کشورهایی که بیمار از آن‌ها می‌آید")
add("languages", "языков", "idiomas", "langues", "زبانیں", "زبان")
add("Hospital tour", "Экскурсия по больнице", "Recorrido por el hospital", "Visite de l’hôpital", "ہسپتال کا دورہ", "بازدید بیمارستان")
add("Take a look inside", "Посмотрите внутри", "Mire el interior", "Regardez à l’intérieur", "اندر جھانکیں", "درون را ببینید")
add(
    "The hospital’s official introduction video: the building, operating rooms, intensive care, imaging and rehabilitation.",
    "Официальный ознакомительный ролик больницы: здание, операционные, реанимация, визуализация и реабилитация.",
    "El vídeo oficial de presentación del hospital: el edificio, los quirófanos, los cuidados intensivos, la imagen y la rehabilitación.",
    "La vidéo officielle de présentation de l’hôpital : le bâtiment, les blocs, la réanimation, l’imagerie et la rééducation.",
    "ہسپتال کی سرکاری تعارفی ویڈیو: عمارت، آپریشن تھیٹر، انتہائی نگہداشت، امیجنگ اور بحالی۔",
    "ویدیوی معرفی رسمی بیمارستان: ساختمان، اتاق‌های عمل، مراقبت ویژه، تصویربرداری و توانبخشی.",
)
# fix hospital's if curly - add both later if needed
add("Biruni University Hospital: introduction video", "Больница Университета Бируни: ознакомительное видео", "Hospital Universitario Biruni: vídeo de presentación", "Hôpital universitaire Biruni : vidéo de présentation", "Biruni یونیورسٹی ہسپتال: تعارفی ویڈیو", "بیمارستان دانشگاه بیرونی: ویدیوی معرفی")
add("Biruni University Hospital: Arabic introduction video", "Больница Университета Бируни: ознакомительное видео на арабском", "Hospital Universitario Biruni: vídeo de presentación en árabe", "Hôpital universitaire Biruni : vidéo de présentation en arabe", "Biruni یونیورسٹی ہسپتال: عربی تعارفی ویڈیو", "بیمارستان دانشگاه بیرونی: ویدیوی معرفی عربی")
add("Facilities & technology", "Отделения и оборудование", "Instalaciones y tecnología", "Plateau technique", "سہولیات اور ٹیکنالوجی", "امکانات و فناوری")
add("Inside the hospital: facilities and technology", "Внутри больницы: отделения и оборудование", "Dentro del hospital: instalaciones y tecnología", "Dans l’hôpital : installations et technologie", "ہسپتال کے اندر: سہولیات اور ٹیکنالوجی", "درون بیمارستان: امکانات و فناوری")
add(
    f"Images and figures from Biruni University Hospital{A}s official introduction video.",
    "Кадры и цифры из официального ознакомительного видео больницы Университета Бируни.",
    "Imágenes y cifras del vídeo oficial de presentación del Hospital Universitario Biruni.",
    "Images et chiffres de la vidéo officielle de présentation de l’Hôpital universitaire Biruni.",
    "Biruni یونیورسٹی ہسپتال کی سرکاری تعارفی ویڈیو سے تصاویر اور اعداد۔",
    "تصویرها و عددها از ویدیوی معرفی رسمی بیمارستان دانشگاه بیرونی.",
)
add("20 operating rooms", "20 операционных", "20 quirófanos", "20 salles d’opération", "20 آپریشن تھیٹر", "۲۰ اتاق عمل")
add("Including a hybrid operating room for cardiovascular, neuro and oncology surgery.", "В том числе гибридная операционная для сердечно-сосудистой, нейро- и онкохирургии.", "Incluido un quirófano híbrido para cirugía cardiovascular, neurocirugía y oncología.", "Dont un bloc hybride pour la chirurgie cardiovasculaire, neurologique et oncologique.", "دل، اعصاب اور آنکولوجی سرجری کے لیے ایک ہائبرڈ آپریشن تھیٹر سمیت۔", "از جمله یک اتاق عمل هیبرید برای جراحی قلب و عروق، مغز و اعصاب و انکولوژی.")
add("100-bed intensive care", "Реанимация на 100 коек", "Cuidados intensivos de 100 camas", "Réanimation de 100 lits", "100 بستر انتہائی نگہداشت", "مراقبت ویژه با ۱۰۰ تخت")
add("Neonatal, pediatric and adult intensive care units.", "Отделения реанимации для новорождённых, детей и взрослых.", "Unidades de cuidados intensivos neonatal, pediátrica y de adultos.", "Réanimations néonatale, pédiatrique et adulte.", "نوزائیدہ، بچوں اور بالغوں کی انتہائی نگہداشت۔", "مراقبت ویژهٔ نوزادان، کودکان و بزرگسالان.")
add("3 Tesla MRI", "МРТ 3 Тесла", "RM de 3 teslas", "IRM 3 teslas", "3 ٹیسلا ایم آر آئی", "ام‌آرآی ۳ تسلا")
add("High-resolution imaging for neurology, oncology and orthopedics.", "Изображения высокого разрешения для неврологии, онкологии и ортопедии.", "Imagen de alta resolución para neurología, oncología y ortopedia.", "Imagerie haute résolution pour la neurologie, l’oncologie et l’orthopédie.", "اعصاب، آنکولوجی اور آرتھوپیڈکس کے لیے ہائی ریزولوشن امیجنگ۔", "تصویر با وضوح بالا برای نورولوژی، انکولوژی و ارتوپدی.")
add("Nuclear-medicine imaging that combines function and anatomy.", "Ядерно-медицинская визуализация, которая совмещает функцию и анатомию.", "Imagen de medicina nuclear que combina función y anatomía.", "Imagerie de médecine nucléaire qui associe fonction et anatomie.", "نیوکلئر میڈیسن کی امیجنگ جو کام اور ساخت کو جوڑتی ہے۔", "تصویر پزشکی هسته‌ای که کارکرد و کالبد را با هم نشان می‌دهد.")
add("Cardiac CT", "КТ сердца", "TC cardíaca", "Scanner cardiaque", "دل کی سی ٹی", "سی‌تی قلب")
add("Non-invasive imaging of the heart and coronary arteries.", "Неинвазивная визуализация сердца и коронарных артерий.", "Imagen no invasiva del corazón y las arterias coronarias.", "Imagerie non invasive du cœur et des artères coronaires.", "دل اور کورونری شریانوں کی بغیر مداخلت امیجنگ۔", "تصویر غیرتهاجمی قلب و سرخرگ‌های کرونر.")
add("Robotic orthopedic surgery", "Роботическая ортопедическая хирургия", "Cirugía ortopédica robótica", "Chirurgie orthopédique robotique", "روبوٹک آرتھوپیڈک سرجری", "جراحی ارتوپدی رباتیک")
add("Robot-assisted joint surgery for suitable patients.", "Робот-ассистированные операции на суставах для подходящих пациентов.", "Cirugía articular asistida por robot para pacientes adecuados.", "Chirurgie articulaire assistée par robot pour les patients adaptés.", "مناسب مریضوں کے لیے روبوٹ کی مدد سے جوڑوں کی سرجری۔", "جراحی مفصل با کمک ربات برای بیماران مناسب.")
add("Robotic rehabilitation center", "Центр роботической реабилитации", "Centro de rehabilitación robótica", "Centre de rééducation robotique", "روبوٹک بحالی مرکز", "مرکز توانبخشی رباتیک")
add("Robot-assisted rehabilitation for children and adults.", "Реабилитация с роботом для детей и взрослых.", "Rehabilitación asistida por robot para niños y adultos.", "Rééducation assistée par robot pour enfants et adultes.", "بچوں اور بالغوں کے لیے روبوٹ کی مدد سے بحالی۔", "توانبخشی با کمک ربات برای کودک و بزرگسال.")
add("Liver & kidney transplant units", "Отделения трансплантации печени и почки", "Unidades de trasplante de hígado y riñón", "Unités de transplantation hépatique et rénale", "جگر اور گردے کی پیوند کاری کے یونٹ", "بخش‌های پیوند کبد و کلیه")
add("Transplant programs for adults and children, under Turkish law.", "Программы трансплантации для взрослых и детей по законодательству Турции.", "Programas de trasplante para adultos y niños, conforme a la ley turca.", "Programmes de transplantation pour adultes et enfants, selon le droit turc.", "بالغوں اور بچوں کے لیے پیوند کاری کے پروگرام، ترکی کے قانون کے تحت۔", "برنامه‌های پیوند برای بزرگسال و کودک، طبق قانون ترکیه.")
add("Patients travelling from abroad", "Пациенты, которые приезжают из-за рубежа", "Pacientes que viajan desde el extranjero", "Patients qui voyagent depuis l’étranger", "بیرون ملک سے آنے والے مریض", "بیمارانی که از خارج سفر می‌کنند")
add("What we arrange before you arrive and after you return", "Что мы организуем до приезда и после возвращения", "Qué organizamos antes de su llegada y después de su regreso", "Ce que nous organisons avant votre arrivée et après votre retour", "آمد سے پہلے اور واپسی کے بعد ہم کیا بندوبست کرتے ہیں", "آنچه پیش از آمد و پس از بازگشت هماهنگ می‌کنیم")
add("Languages", "Языки", "Idiomas", "Langues", "زبانیں", "زبان‌ها")
add(
    "A coordinator in your language from the first message, report translation and interpreting in hospital.",
    "Координатор на вашем языке с первого сообщения, перевод заключений и устный перевод в больнице.",
    "Un coordinador en su idioma desde el primer mensaje, traducción de informes e interpretación en el hospital.",
    "Un coordinateur dans votre langue dès le premier message, traduction des comptes rendus et interprétation à l’hôpital.",
    "پہلے پیغام سے آپ کی زبان میں کوآرڈینیٹر، رپورٹوں کا ترجمہ اور ہسپتال میں ترجمانی۔",
    "هماهنگ‌کننده به زبان شما از نخستین پیام، ترجمهٔ گزارش‌ها و ترجمهٔ شفاهی در بیمارستان.",
)
add("Practical arrangements", "Практические вопросы", "Gestiones prácticas", "Organisation pratique", "عملی بندوبست", "هماهنگی عملی")
add(
    "Visa invitation letter, airport pick-up and private transfer, hotel or in-hospital stay for patient and companion.",
    "Приглашение для визы, встреча в аэропорту и индивидуальный трансфер, гостиница или пребывание в больнице для пациента и сопровождающего.",
    "Carta de invitación para el visado, recogida en el aeropuerto y traslado privado, hotel o estancia en el hospital para el paciente y el acompañante.",
    "Lettre d’invitation pour le visa, accueil à l’aéroport et transfert privé, hôtel ou séjour à l’hôpital pour le patient et l’accompagnant.",
    "ویزا دعوت نامہ، ہوائی اڈے سے استقبال اور نجی ٹرانسفر، مریض اور ساتھی کے لیے ہوٹل یا ہسپتال میں قیام۔",
    "دعوت‌نامهٔ ویزا، استقبال فرودگاه و انتقال اختصاصی، هتل یا اقامت در بیمارستان برای بیمار و همراه.",
)
add("Follow-up at home", "Наблюдение дома", "Seguimiento en casa", "Suivi à la maison", "گھر پر فالو اپ", "پیگیری در خانه")
add(
    "A detailed discharge summary, remote follow-up and contact with your local doctor.",
    "Подробный выписной эпикриз, дистанционное наблюдение и связь с вашим местным врачом.",
    "Un informe de alta detallado, seguimiento a distancia y contacto con su médico local.",
    "Un compte rendu de sortie détaillé, un suivi à distance et le contact avec votre médecin local.",
    "تفصیلی ڈسچارج خلاصہ، دور سے فالو اپ، اور آپ کے مقامی معالج سے رابطہ۔",
    "خلاصهٔ ترخیص دقیق، پیگیری از راه دور و تماس با پزشک محل زندگی شما.",
)
add(
    "Our physicians are faculty members at Biruni University Faculty of Medicine, involved in research, publications and continuing medical education. Academic medicine means your treatment is built on evidence.",
    "Наши врачи — преподаватели медицинского факультета Университета Бируни: они участвуют в исследованиях, публикациях и непрерывном образовании. Академическая медицина означает, что лечение опирается на данные.",
    "Nuestros médicos son docentes de la Facultad de Medicina de la Universidad Biruni y participan en investigación, publicaciones y formación continuada. La medicina académica significa que el tratamiento se apoya en la evidencia.",
    "Nos médecins sont enseignants à la Faculté de médecine de l’Université Biruni et participent à la recherche, aux publications et à la formation continue. La médecine universitaire signifie que le traitement s’appuie sur des données.",
    "ہمارے معالج Biruni یونیورسٹی فیکلٹی آف میڈیسن کے اراکین ہیں، تحقیق، اشاعتوں اور مسلسل طبی تعلیم میں۔ تعلیمی طب کا مطلب ہے کہ علاج شواہد پر کھڑا ہو۔",
    "پزشکان ما عضو هیئت علمی دانشکدهٔ پزشکی دانشگاه بیرونی‌اند و در پژوهش، انتشار و آموزش مداوم پزشکی شرکت دارند. پزشکی دانشگاهی یعنی درمان بر شواهد استوار است.",
)
add("Before you choose", "Прежде чем выбрать", "Antes de elegir", "Avant de choisir", "انتخاب سے پہلے", "پیش از انتخاب")
add("How to judge a hospital", "Как оценивать больницу", "Cómo valorar un hospital", "Comment juger un hôpital", "ہسپتال کو کیسے جانچیں", "چگونه بیمارستان را بسنجیم")
add("from abroad", "из-за рубежа", "desde el extranjero", "depuis l’étranger", "بیرون ملک سے", "از خارج")
add(
    "Ask any hospital these questions before you travel. We answer them in writing.",
    "Задайте любой больнице эти вопросы до поездки. Мы отвечаем на них письменно.",
    "Haga estas preguntas a cualquier hospital antes de viajar. Nosotros las respondemos por escrito.",
    "Posez ces questions à n’importe quel hôpital avant de voyager. Nous y répondons par écrit.",
    "سفر سے پہلے کسی بھی ہسپتال سے یہ سوال پوچھیں۔ ہم تحریری جواب دیتے ہیں۔",
    "پیش از سفر این پرسش‌ها را از هر بیمارستانی بپرسید. ما کتبی پاسخ می‌دهیم.",
)
add(
    "Is it authorized by the Ministry of Health for international health tourism?",
    "Есть ли у неё разрешение Министерства здравоохранения на международный медицинский туризм?",
    "¿Está autorizado por el Ministerio de Salud para el turismo de salud internacional?",
    "Est-il autorisé par le ministère de la Santé pour le tourisme médical international ?",
    "کیا وزارتِ صحت نے اسے بین الاقوامی صحت سیاحت کے لیے مجاز کیا ہے؟",
    "آیا وزارت بهداشت آن را برای گردشگری سلامت بین‌المللی مجاز کرده است؟",
)
add("Who decides my plan: one doctor or a team?", "Кто решает план: один врач или команда?", "¿Quién decide mi plan: un médico o un equipo?", "Qui décide de mon plan : un médecin ou une équipe ?", "منصوبہ کون بناتا ہے: ایک معالج یا ٹیم؟", "برنامه را چه کسی تعیین می‌کند: یک پزشک یا یک تیم؟")
add("Does the written estimate say what is and is not included?", "Указано ли в письменной смете, что входит и что не входит?", "¿El presupuesto escrito dice qué está incluido y qué no?", "Le devis écrit précise-t-il ce qui est inclus et ce qui ne l’est pas ?", "کیا تحریری تخمینہ بتاتا ہے کہ کیا شامل ہے اور کیا نہیں؟", "آیا برآورد کتبی می‌گوید چه چیزی هست و چه چیزی نیست؟")
add("How will follow-up work after I return?", "Как будет устроено наблюдение после возвращения?", "¿Cómo será el seguimiento cuando regrese?", "Comment se fera le suivi après mon retour ?", "واپسی کے بعد فالو اپ کیسے ہوگا؟", "پیگیری پس از بازگشت چگونه است؟")
add("International patient service of Biruni University Hospital", "Международная служба пациентов больницы Университета Бируни", "Servicio de pacientes internacionales del Hospital Universitario Biruni", "Service des patients internationaux de l’Hôpital universitaire Biruni", "Biruni یونیورسٹی ہسپتال کی بین الاقوامی مریض سروس", "خدمات بیماران بین‌المللی بیمارستان دانشگاه بیرونی")
add("Questions about Biruni Bridge", "Вопросы о Biruni Bridge", "Preguntas sobre Biruni Bridge", "Questions sur Biruni Bridge", "Biruni Bridge کے بارے میں سوالات", "پرسش‌ها دربارهٔ بیرونی بریج")
add("Is Biruni Bridge a separate hospital?", "Biruni Bridge — это отдельная больница?", "¿Biruni Bridge es un hospital aparte?", "Biruni Bridge est-il un hôpital distinct ?", "کیا Biruni Bridge الگ ہسپتال ہے؟", "آیا بیرونی بریج بیمارستان جداگانه‌ای است؟")
add("No. It is the international patient service of Biruni University Hospital.", "Нет. Это служба для иностранных пациентов больницы Университета Бируни.", "No. Es el servicio de pacientes internacionales del Hospital Universitario Biruni.", "Non. C’est le service des patients internationaux de l’Hôpital universitaire Biruni.", "نہیں۔ یہ Biruni یونیورسٹی ہسپتال کی بین الاقوامی مریض سروس ہے۔", "خیر. این خدمات بیماران بین‌المللی بیمارستان دانشگاه بیرونی است.")
add("Where is the hospital?", "Где находится больница?", "¿Dónde está el hospital?", "Où se trouve l’hôpital ?", "ہسپتال کہاں ہے؟", "بیمارستان کجاست؟")
add(
    "In Küçükçekmece, on the European side of Istanbul, easy to reach from Istanbul Airport and Sabiha Gökçen.",
    "В Кючюкчекмедже, на европейской стороне Стамбула, удобно добираться из аэропортов Стамбул и Сабиха Гёкчен.",
    "En Küçükçekmece, en la parte europea de Estambul, con buen acceso desde el aeropuerto de Estambul y Sabiha Gökçen.",
    "À Küçükçekmece, sur la rive européenne d’Istanbul, facile d’accès depuis l’aéroport d’Istanbul et Sabiha Gökçen.",
    "Küçükçekmece میں، استنبول کے یورپی کنارے پر، استنبول ایئرپورٹ اور صبیحہ گوکچن سے آسان رسائی۔",
    "در کوچک‌چکمجه، سمت اروپایی استانبول، با دسترسی آسان از فرودگاه استانبول و صبیحه گوکچن.",
)
add("Can my companion stay with me?", "Может ли сопровождающий остаться со мной?", "¿Puede quedarse mi acompañante conmigo?", "Mon accompagnant peut-il rester avec moi ?", "کیا میرا ساتھی میرے ساتھ رہ سکتا ہے؟", "آیا همراهم می‌تواند پیش من بماند؟")
add(f"Yes, under the hospital{A}s companion policy.", "Да, по правилам больницы для сопровождающих.", "Sí, según la política de acompañantes del hospital.", "Oui, selon la politique d’accompagnement de l’hôpital.", "ہاں، ہسپتال کی ساتھی پالیسی کے تحت۔", "بله، طبق مقررات همراه بیمارستان.")
add("Start by sending your report", "Начните с отправки документов", "Empiece enviando su informe", "Commencez par envoyer votre dossier", "اپنی رپورٹ بھیج کر آغاز کریں", "با فرستادن گزارش شروع کنید")
add("A coordinator who speaks your language will explain the next steps.", "Координатор, который говорит на вашем языке, объяснит следующие шаги.", "Un coordinador que habla su idioma le explicará los siguientes pasos.", "Un coordinateur qui parle votre langue vous expliquera la suite.", "آپ کی زبان بولنے والا کوآرڈینیٹر اگلے قدم بتائے گا۔", "هماهنگ‌کننده‌ای که به زبان شما صحبت می‌کند گام بعدی را توضیح می‌دهد.")
add(
    "Biruni University Hospital in Istanbul: a university hospital since 2016 on 80,000 m², with an international team serving patients from 118+ countries.",
    "Больница Университета Бируни в Стамбуле: университетская больница с 2016 года на 80 000 м², международная команда принимает пациентов из 118+ стран.",
    "Hospital Universitario Biruni en Estambul: hospital universitario desde 2016 en 80.000 m², con un equipo internacional que atiende a pacientes de más de 118 países.",
    "Hôpital universitaire Biruni à Istanbul : hôpital universitaire depuis 2016 sur 80 000 m², avec une équipe internationale qui reçoit des patients de plus de 118 pays.",
    "استنبول میں Biruni یونیورسٹی ہسپتال: 2016 سے یونیورسٹی ہسپتال، 80,000 مربع میٹر، بین الاقوامی ٹیم 118 سے زیادہ ممالک کے مریضوں کی خدمت کرتی ہے۔",
    "بیمارستان دانشگاه بیرونی در استانبول: بیمارستان دانشگاهی از ۲۰۱۶ در ۸۰٬۰۰۰ مترمربع، با تیم بین‌المللی برای بیماران بیش از ۱۱۸ کشور.",
)
add("international patient services", "служба для иностранных пациентов", "servicios para pacientes internacionales", "services aux patients internationaux", "بین الاقوامی مریضوں کی خدمات", "خدمات بیماران بین‌المللی")
add("Arabic", "арабский", "árabe", "arabe", "عربی", "عربی")
add("English", "английский", "inglés", "anglais", "انگریزی", "انگلیسی")
add("French", "французский", "francés", "français", "فرانسیسی", "فرانسوی")
add("Russian", "русский", "ruso", "russe", "روسی", "روسی")
add("Persian", "персидский", "persa", "persan", "فارسی", "فارسی")
add("Spanish", "испанский", "español", "espagnol", "ہسپانوی", "اسپانیایی")
add("Urdu", "урду", "urdu", "ourdou", "اردو", "اردو")
add("Biruni Bridge – international patient service", "Biruni Bridge — служба для иностранных пациентов", "Biruni Bridge – servicio de pacientes internacionales", "Biruni Bridge – service des patients internationaux", "Biruni Bridge – بین الاقوامی مریض سروس", "بیرونی بریج – خدمات بیماران بین‌المللی")
add(
    "TEMOS International Healthcare Accreditation – Quality in Medical Care (first issued June 2024, valid until May 2027)",
    "TEMOS International Healthcare Accreditation — качество медицинской помощи (впервые выдан в июне 2024, действителен до мая 2027)",
    "TEMOS International Healthcare Accreditation – calidad en la atención médica (primera emisión junio de 2024, válido hasta mayo de 2027)",
    "TEMOS International Healthcare Accreditation – qualité des soins médicaux (première délivrance juin 2024, valable jusqu’en mai 2027)",
    "TEMOS International Healthcare Accreditation – طبی دیکھ بھال میں معیار (پہلی بار جون 2024، مئی 2027 تک)",
    "TEMOS International Healthcare Accreditation – کیفیت مراقبت پزشکی (نخستین صدور ژوئن ۲۰۲۴، معتبر تا مه ۲۰۲۷)",
)
add(
    "Diplomatic Council – Preferred Partner Hospital (first accredited June 2024, valid until May 2027)",
    "Diplomatic Council — предпочтительная больница-партнёр (первая аккредитация июнь 2024, действителен до мая 2027)",
    "Diplomatic Council – hospital socio preferente (primera acreditación junio de 2024, válido hasta mayo de 2027)",
    "Diplomatic Council – hôpital partenaire privilégié (première accréditation juin 2024, valable jusqu’en mai 2027)",
    "Diplomatic Council – ترجیحی پارٹنر ہسپتال (پہلی سند جون 2024، مئی 2027 تک)",
    "Diplomatic Council – بیمارستان همکار برگزیده (نخستین اعتبار ژوئن ۲۰۲۴، معتبر تا مه ۲۰۲۷)",
)
add("TEMOS International Healthcare Accreditation – Quality in Medical Care", "TEMOS International Healthcare Accreditation — качество медицинской помощи", "TEMOS International Healthcare Accreditation – calidad en la atención médica", "TEMOS International Healthcare Accreditation – qualité des soins médicaux", "TEMOS International Healthcare Accreditation – طبی دیکھ بھال میں معیار", "TEMOS International Healthcare Accreditation – کیفیت مراقبت پزشکی")
add("Diplomatic Council Preferred Partner Hospital", "Diplomatic Council: предпочтительная больница-партнёр", "Diplomatic Council hospital socio preferente", "Diplomatic Council hôpital partenaire privilégié", "Diplomatic Council ترجیحی پارٹنر ہسپتال", "Diplomatic Council بیمارستان همکار برگزیده")
add("International patient service of Biruni University Hospital, Istanbul", "Служба для иностранных пациентов больницы Университета Бируни, Стамбул", "Servicio de pacientes internacionales del Hospital Universitario Biruni, Estambul", "Service des patients internationaux de l’Hôpital universitaire Biruni, Istanbul", "Biruni یونیورسٹی ہسپتال، استنبول کی بین الاقوامی مریض سروس", "خدمات بیماران بین‌المللی بیمارستان دانشگاه بیرونی، استانبول")
add("TEMOS certificate", "Сертификат TEMOS", "Certificado TEMOS", "Certificat TEMOS", "TEMOS سرٹیفکیٹ", "گواهی TEMOS")
