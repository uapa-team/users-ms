# Seeding
from django_seed import Seed
from uapapp.models import Dependencia, Programa

dependencias = ["Área curricular de ingniería civil y agrícola",
                 "Área curricular de ingniería química y ambiental", 
                 "Área curricular de ingniería mecánica y mecatrónica", 
                 "Área curricular de ingniería eléctrica y electrónica",
                 "Área curricular de ingniería sistemas e industrial",
                ]

programasPre = ["Ingeniería Civil", "Ingeniería Agrícola", 
                "Ingeniería Química", 
                "Ingeniería Mecánica", "Ingeniería Mecatrónica", 
                "Ingeniería Eléctrica","Ingeniería Electrónica", 
                "Ingeniería de Sistemas y Computación", "Ingeniería Industrial"
                ]

programasPos = ["Especialización en Calidad de la Energía","Especialización en Ingeniería Eléctrica","Especialización en Geotecnia","Especialización en Recursos Hidráulicos","Especialización en Transporte","Especialización en Ingeniería - Tránsito, Diseño y Seguridad Vial","Maestría en Ingeniería - Ingeniería Ambiental","Doctorado en Ingeniería - Ciencia y Tecnología de Materiales","Doctorado en Ingeniería - Geotecnia","Doctorado en Ingeniería - Sistemas y Computación","Doctorado en Ingeniería - Ingeniería Eléctrica","Doctorado en Ingeniería - Ingeniería Química","Especialización en Automatización Industrial","Especialización en Iluminación Pública y Privada","Especialización en Transito, Diseño y Seguridad Vial","Maestría en Ingeniería - Automatización Industrial","Maestría en Ingeniería - Estructuras","Maestría en Ingeniería - Geotecnia","Maestría en Ingeniería - Ingeniería Agrícola","Maestría en Ingeniería - Ingeniería de Sistemas y Computación","Maestría en Ingeniería - Ingeniería Eléctrica","Maestría en Ingeniería - Ingeniería Química","Maestría en Ingeniería - Recursos Hidráulicos","Maestría en Ingeniería - Transporte","Maestría en Ingeniería - Telecomunicaciones","Maestría en Ingenieria Industrial","Maestría en Ingeniería - Ingeniería Mecánica","Maestría en Ingeniería - Materiales y Procesos","Especialización en Ingeniería Ambiental","Maestría en Ingeniería - Ingeniería Eléctrica Convenio Sede Manizales","Doctorado en Ingeniería - Industria y Organizaciones","Doctorado en Ingeniería - Ingeniería Mecánica y Mecatrónica","Maestría en Ingeniería - Ingeniería de Sistemas y Computación - Conv UPC","Maestría en Ingeniería - Ingeniería Electrónica","Maestría en Bioinformática","Especialización en Estructuras","Doctorado en Ingeniería - Ingeniería Civil","Especialización en Gobierno Electrónico","Maestría en Ingeniería - Ingeniería de Sistemas y Computación - Conv Unillanos","Doctorado en Estudios Ambientales"]