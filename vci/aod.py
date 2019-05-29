import xarray as xr
import numpy as np
import pandas as pd
from typing import NamedTuple


class Volcano(NamedTuple):
    name: str
    date: str
    latitude: float
    longitude: float
    altitude: float
    so2: float
    measurement: str


volcanoes = [
    Volcano('Nyamuragira', '23-07-2002', -1, 30, 15, 23, 'M'),
    Volcano('Witori', '02-08-2002', -6, 150, 14, 18, 'M'),
    Volcano('Ruang', '26-10-2002', 2, 125, 18, 71, 'MG'),
    Volcano('El Reventador', '05-11-2002', 0, -78, 17, 77, 'MG'),
    Volcano('Nyiragongo', '09-01-2003', -1, 30, 15, 20, 'MG'),
    Volcano('Lokon', '09-01-2003', 1, 125, 16, 17, 'MG'),
    Volcano('Nyirag', '05-03-2003', -5, 30, 17, 17, 'MG'),
    Volcano('Lokon(Rabaul?)', '05-03-2003', 1, 125, 15, 19, 'MG'),
    Volcano('Anatahan', '14-05-2003', 16, 143, 16, 13, 'M'),
    Volcano('Nyirag', '14-05-2003', -1, 30, 16, 21, 'M'),
    Volcano('Ulawun', '14-05-2003', -5, 150, 17, 9, 'M'),    Volcano('Lewotobi', '13-06-2003', -8, 123, 15, 13, 'MG'),
    Volcano('Kanlaon', '13-06-2003', 10, 123, 15, 21, 'MG'),
    Volcano('Soufriere Hills', '13-07-2003', 16, -62, 16.5, 59, 'MG'),
    Volcano('Gamalama, Japan', '17-08-2003', 1, 128, 16, 15, 'MG'),
    Volcano('Gamalama, Japan', '17-08-2003', 33, 131, 16, 13, 'MG'),
    Volcano('Bezymianny or Klyuchev', '06-10-2003', 56, 160, 14, 8, 'G'),
    Volcano('Lokon', '26-10-2003', 2, 125, 16, 12, 'MG'),
    Volcano('Soufriere Hills', '26-10-2003', 15, -62, 16, 9, 'MG'),
    Volcano('Rabaul', '10-11-2003', -5, 150, 16, 24, 'MG'),
    Volcano('Rabaul', '05-12-2003', -5, 150, 16, 19, 'MG'),
    Volcano('Rabaul', '09-01-2004', -5, 150, 17, 15, 'MG'),
    Volcano('Nyiragongo?', '09-01-2004', -1, 30, 15, 13, 'MG'),
    Volcano('Langila', '03-02-2004', -5, 150, 17, 4, 'MG'),
    Volcano('Nyiragongo?', '03-02-2004', -1, 30, 17, 4, 'MG'),
    Volcano('Soufriere Hills', '04-03-2004', 10, -62, 17, 28, 'MG'),
    Volcano('Nyamu', '12-06-2004', -1, 30, 17, 25, 'G'),
    Volcano('Awu', '12-06-2004', 4, 125, 15, 22, 'G'),
    Volcano('Tengger C.', '12-06-2004', -8, 112, 15, 22, 'G'),
    Volcano('Pacaya', '17-07-2004', 15, -91, 17, 16, 'G'),
    Volcano('Galeras', '17-07-2004', 1, -77, 17, 15, 'G'),
    Volcano('Galeras', '11-08-2004', 1, -77, 16, 21, 'G'),
    Volcano('Vanuatu', '30-09-2004', -16, 168, 15, 10, 'G'),
    Volcano('Rinjani', '30-09-2004', -8, 116, 15, 21 / 2, 'G'),
    Volcano('Kerinci', '30-09-2004', -2, 101, 17, 21 / 2, 'G'),
    Volcano('Manam', '30-10-2004', -4, 144, 16, 11, 'G'),
    Volcano('Soputan', '30-10-2004', 1, 125, 16, 16, 'G'),
    Volcano('Manam', '24-11-2004', -4, 144, 17, 22, 'G'),
    Volcano('Nyiragongo', '24-11-2004', -1, 30, 15, 14, 'G'),
    Volcano('Nyiaragongo', '04-12-2004', 0, 30, 16, 31, 'G'),
    Volcano('Reventador', '04-12-2004', 0, -77, 16, 8, 'G'),
    Volcano('Vanuatu', '24-12-2004', -16, 168, 17, 22, 'G'),
    Volcano('Soputan', '24-12-2004', 1, 125, 15, 23, 'G'),
    Volcano('Manam', '28-01-2005', -4, 144, 18, 144, 'MG, M(*)'),
    Volcano('Anatahan', '03-04-2005', 16, 143, 15, 21, 'M'),
    Volcano('Anatahan', '23-04-2005', 16, 143, 16, 30, 'M'),
    Volcano('Soufriere Hills', '23-04-2005', 16, -62, 16, 30, 'M'),
    Volcano('Anatahan', '18-05-2005', 16, 143, 15, 11, 'M'),
    Volcano('Fernadina', '18-05-2005', 0, -91, 15, 15, 'M'),
    Volcano('Van.', '18-05-2005', -16, 168, 15, 8, 'M'),
    Volcano('Anatahan', '12-06-2005', 16, 143, 15, 17, 'M'),
    Volcano('Santa Ana', '12-06-2005', 14, -90, 15, 13, 'M'),
    Volcano('Anatahan', '12-07-2005', 16, 143, 15, 18, 'M'),
    Volcano('Soufriere Hills', '12-07-2005', 16, -62, 15, 13, 'M'),
    Volcano('Anatahan', '06-08-2005', 16, 143, 15, 19, 'M'),
    Volcano('Raung', '06-08-2005', -8, 113, 15, 28, 'M'),
    Volcano('Anatahan', '16-08-2005', 16, 143, 15, 25, 'MG'),
    Volcano('Raung', '16-08-2005', -8, 113, 15, 31, 'MG'),
    Volcano('Santa Ana', '05-10-2005', 14, -90, 17, 46, 'M'),
    Volcano('Sierra Negra', '25-10-2005', -1, -91, 15, 20, 'G'),
    Volcano('Dabbahu', '25-10-2005', -13, 40, 15, 27, 'G'),
    Volcano('Karthala', '24-11-2005', -10, 43, 16, 16, 'MG'),
    Volcano('Galeras', '24-11-2005', -2, -80, 16, 14, 'MG'),
    Volcano('Soputan', '24-12-2005', 1, 125, 16, 33, 'MG'),
    Volcano('Lopevi', '24-12-2005', -16, 168, 16, 18, 'MG'),
    Volcano('Rabaul', '23-01-2006', -5, 152, 16, 31, 'MG'),
    Volcano('Manam', '04-03-2006', -5, 144, 17, 72, 'MG'),
    Volcano('Chile', '04-03-2006', -40, -70, 17, 7, 'MG'),
    Volcano('Cleveland', '14-03-2006', 53, -170, 13, 8, 'G'),
    Volcano('Ecuad.', '18-04-2006', -5, -78, 17, 16, 'M'),
    Volcano('Tinakula', '18-04-2006', -10, 166, 17, 21, 'M'),
    Volcano('Lascar', '18-04-2006', -23, -68, 17, 3, 'M'),
    Volcano('Soufriere Hills', '23-05-2006', 16, -62, 19, 156, 'MG'),
    Volcano('Kanlaon', '02-07-2006', 10, 123, 20, 70, 'M'),
    Volcano('Tungurahua', '16-08-2006', -2, -78, 19, 44, 'MG'),
    Volcano('Rabaul', '16-08-2006', -4, 150, 19, 22, 'MG'),
    Volcano('Rabaul', '10-10-2006', -4, 150, 17, 172, 'M'),
    Volcano('Ubinas', '25-10-2006', -20, -70, 17, 14, 'M'),
    Volcano('Vanuatu', '25-10-2006', -20, 168, 15, 41, 'M'),
    Volcano('Ambrym', '09-11-2006', -10, 160, 17, 45, 'M'),
    Volcano('Nyamuragira', '29-11-2006', 5, 30, 17, 40, 'MG'),
    Volcano('Mexico', '29-11-2006', 5, -90, 15, 30, 'MG'),
    Volcano('Bulusan', '24-12-2006', 13, 125, 18, 10, 'MG'),
    Volcano('Soputan', '24-12-2006', 1, 125, 16, 10, 'MG'),
    Volcano('Vanuatu', '24-12-2006', -16, 168, 15, 18, 'MG'),
    Volcano('Karthala', '23-01-2007', -10, 43, 17, 6, 'MG'),
    Volcano('Bulusan', '23-01-2007', 13, 125, 17, 5, 'MG'),
    Volcano('Lascar', '23-01-2007', -23, -68, 15, 7, 'MG'),
    Volcano('Shiveluch', '23-01-2007', 57, 160, 15, 8, 'MG'),
    Volcano('Vanuatu', '23-01-2007', -16, 168, 15, 6, 'MG'),
    Volcano('Nev.d Huila', '22-02-2007', 0, -70, 16, 11, 'MG'),
    Volcano('Kartha.', '22-02-2007', -10, 43, 15, 14, 'MG'),
    Volcano('Van.', '22-02-2007', -16, 168, 16, 11, 'MG'),
    Volcano('Etna', '24-03-2007', 38, 15, 15, 11, 'MG'),
    Volcano('Reventador', '24-03-2007', 0, -78, 16, 24, 'MG'),
    Volcano('Ambrym', '24-03-2007', -16, 160, 17, 20, 'MG'),
    Volcano('Pit.Fourn.Reunion', '08-04-2007', -20, 57, 16, 31, 'MG'),
    Volcano('Reventador', '08-04-2007', 0, -80, 16, 15, 'MG'),
    Volcano('Ulawun', '03-05-2007', -5, 150, 15, 15, 'MG'),
    Volcano('Vanuatu', '03-05-2007', -25, 160, 15, 7, 'MG'),
    Volcano('N.d.Huila', '03-05-2007', 3, -70, 15, 9, 'MG'),
    Volcano('Papua', '13-05-2007', -10, 150, 16, 8, 'MG'),
    Volcano('Kamchatka', '13-05-2007', 50, 150, 16, 1, 'MG'),
    Volcano('Nyira.', '13-05-2007', 0, 30, 16, 13, 'MG'),
    Volcano('Ubinas + Lascar', '13-05-2007', -20, -75, 16, 8, 'MG'),
    Volcano('Llaima', '23-05-2007', -30, -70, 18, 14, 'MG'),
    Volcano('Vanuatu', '23-05-2007', -15, 160, 15, 8, 'MG'),
    Volcano('Bulusan', '23-05-2007', 13, 125, 17, 10, 'MG'),
    Volcano('Soputan', '12-06-2007', 1, 125, 16, 19, 'MG'),
    Volcano('Bezym.', '12-06-2007', 56, 160, 14, 10, 'MG'),
    Volcano('Telica', '12-06-2007', 13, -87, 15, 13, 'MG'),
    Volcano('Lengai', '02-07-2007', 2, 29, 16, 17, 'M'),
    Volcano('Mexico', '02-07-2007', 20, -90, 15, 11, 'M'),
    Volcano('Raung', '27-07-2007', -5, 110, 15, 14, 'M'),
    Volcano('Japan', '27-07-2007', 35, 130, 15, 14, 'M'),
    Volcano('Manda Hararo', '11-08-2007', 12, 40, 17, 21, 'M'),
    Volcano('Java', '11-08-2007', -5, 115, 15, 18, 'M'),
    Volcano('Vanuatu', '20-09-2007', -5, 180, 16, 11, 'M'),
    Volcano('Mexico', '20-09-2007', 20, -90, 16, 18, 'M'),
    Volcano('Jebel al Tair', '05-10-2007', 16, 42, 16, 68, 'M'),
    Volcano('Galeras', '05-10-2007', 1, -80, 16, 13, 'M'),
    Volcano('Galeras', '04-11-2007', -2, -80, 16, 10, 'MG'),
    Volcano('Jebel al Tair', '04-11-2007', 15, 42, 16, 7, 'MG'),
    Volcano('Soputan', '04-11-2007', -5, 110, 16, 12, 'MG'),
    Volcano('Soputan or Krakatau', '14-11-2007', -5, 110, 16, 13, 'M'),
    Volcano('Galeras', '14-11-2007', -1, -75, 16, 12, 'M'),
    Volcano('Chikurachki', '14-11-2007', 50, 155, 15, 45, 'M'),
    Volcano('Talang', '09-12-2007', 0, 100, 16, 13, 'M'),
    Volcano('Galeras', '09-12-2007', 0, -75, 16, 15, 'M'),
    Volcano('Ulawun', '19-12-2007', 1, 150, 17, 29, 'MG'),
    Volcano('Nevado del Huila', '03-01-2008', 1, -71, 17, 32, 'M'),
    Volcano('Llaima', '03-01-2008', -35, -71, 15, 5, 'M'),
    Volcano('Galeras', '23-01-2008', -3, -80, 16, 24, 'M'),
    Volcano('Anatahan', '23-01-2008', 15, 145, 16, 12, 'M'),
    Volcano('Tungurahua', '12-02-2008', -5, -80, 16, 19, 'M'),
    Volcano('Papua', '12-02-2008', -5, 155, 17, 14, 'M'),
    Volcano('TaraBatu', '13-03-2008', -5, 125, 16, 33, 'MG'),
    Volcano('Lengai', '28-03-2008', -5, 36, 16, 10, 'M'),
    Volcano('Andes', '28-03-2008', 5, -80, 16, 7, 'M'),
    Volcano('Kerinci', '28-03-2008', -2, 101, 16, 11, 'M'),
    Volcano('Egon', '12-04-2008', -5, 122, 15, 20, 'M'),
    Volcano('Nev.d.Huila', '12-04-2008', 5, -76, 17, 13, 'M'),
    Volcano('Mexico', '27-04-2008', 15, -90, 16, 13, 'M'),
    Volcano('Ibu', '27-04-2008', -35, 125, 16, 15, 'M'),
    Volcano('Chaiten', '27-04-2008', -35, -70, 16, 4, 'M'),
    Volcano('Mexico', '12-05-2008', 10, -90, 16, 13, 'M'),
    Volcano('Barren I.', '12-05-2008', -35, 90, 14, 18, 'M'),
    Volcano('Chaiten', '12-05-2008', -35, -70, 14, 6, 'M'),
    Volcano('Soputan', '16-06-2008', 1, 125, 16, 32, 'M'),
    Volcano('Nicaragua / C.R.', '16-06-2008', 15, -85, 16, 10, 'M'),
    Volcano('Okmok', '21-07-2008', 53, -168, 16, 57, 'M'),
    Volcano('Soputan', '21-07-2008', 1, 125, 16, 30, 'M'),
    Volcano('Kasatochi', '15-08-2008', 52, -175, 16, 390, 'MG'),
    Volcano('Dallafilla', '13-11-2008', 14, 40, 17, 55, 'M'),
    Volcano('N.d.Huila.', '13-11-2008', 3, -78, 17, 40, 'M'),
    Volcano('Karangetang', '18-12-2008', 3, 125, 17, 19, 'MG'),
    Volcano('Galeras', '18-12-2008', 0, -80, 17, 13, 'MG'),
    Volcano('Japan', '18-12-2008', 30, 130, 15, 11, 'MG'),
    Volcano('Barren Island', '02-01-2009', 10, 90, 17, 16, 'M'),
    Volcano('Galeras', '02-01-2009', 3, -80, 15, 16, 'M'),
    Volcano('Indonesia?', '27-01-2009', -5, 100, 16, 15, 'M'),
    Volcano('Galeras', '27-01-2009', 0, -80, 16, 13, 'M'),
    Volcano('Galeras', '16-02-2009', -2, -78, 16, 12, 'M'),
    Volcano('Villarrica', '16-02-2009', -35, -75, 15, 7, 'M'),
    Volcano('Karangetang', '16-02-2009', 3, 100, 16, 7, 'M'),
    Volcano('Vanuatu', '16-02-2009', -16, 168, 17, 8, 'M'),
    Volcano('Redoubt', '28-03-2009', 60, -155, 13, 61, 'M'),
    Volcano('Galeras', '28-03-2009', 0, -75, 15, 43, 'M'),
    Volcano('Fernandina.', '12-04-2009', 0, -90, 16, 12, 'M'),
    Volcano('Nyira.', '12-04-2009', 0, 30, 16, 16, 'M'),
    Volcano('Galeras + Reventador', '07-05-2009', 0, -75, 15, 31, 'M'),
    Volcano('Rinjani, ', '22-05-2009', -5, 116, 16, 5, 'M'),
    Volcano('Vanuatu', '22-05-2009', -15, 165, 16, 6, 'M'),
    Volcano('Revent.', '22-05-2009', 3, -80, 16, 18, 'M'),
    Volcano('Sarychev', '21-06-2009', 48, 153, 16, 496, 'MG'),
    Volcano('MandaHararo', '21-06-2009', 12, 40, 16, 91, 'MG'),
    Volcano('Vanuatu', '04-10-2009', -15, 165, 17, 6, 'M'),
    Volcano('Mayon', '04-10-2009', 13, 120, 17, 9, 'M'),
    Volcano('Galeras', '04-10-2009', 2, -80, 17, 14, 'M'),
    Volcano('Tungurahua', '19-10-2009', 5, -76, 16, 11, 'MG'),
    Volcano('Hawaii.', '19-10-2009', 20, -155, 16, 8, 'MG'),
    Volcano('Van.', '19-10-2009', -16, 165, 16, 9, 'MG'),
    Volcano('Galeras', '03-12-2009', 0, -78, 17, 15, 'M'),
    Volcano('Karkar', '03-12-2009', -5, 146, 17, 12, 'M'),
    Volcano('Vanuatu', '03-12-2009', -16, 165, 17, 5, 'M'),
    Volcano('Mayon', '02-01-2010', 13, 120, 16, 12, 'M'),
    Volcano('Nyamuragira', '02-01-2010', 0, 30, 16, 12, 'M'),
    Volcano('Van.', '02-01-2010', -15, 168, 16, 13, 'M'),
    Volcano('Turrialba', '17-01-2010', 5, -82, 16, 15, 'M'),
    Volcano('Vanuatu', '17-01-2010', -15, 168, 16, 15, 'M'),
    Volcano('Soufriere Hills', '16-02-2010', 16, -62, 17, 46, 'M'),
    Volcano('Arenal', '02-04-2010', 9, -84, 15, 18, 'M'),
    Volcano('Indon.', '02-04-2010', 0, 120, 15, 15, 'M'),
    Volcano('Van.', '02-04-2010', -16, 168, 15, 6, 'M'),
    Volcano('Tungurahua', '02-05-2010', -5, -78, 16, 20, 'M'),
    Volcano('Dukono', '02-05-2010', 2, 128, 16, 14, 'M'),
    Volcano('Van.', '02-05-2010', -16, 168, 16, 10, 'M'),
    Volcano('Pacaya', '06-06-2010', 15, -91, 17, 38, 'M'),
    Volcano('Ulawun', '06-06-2010', -5, 150, 16, 8, 'M'),
    Volcano('Sarigan', '06-06-2010', 16, 145, 15, 6, 'M'),
    Volcano('Ulawun', '16-07-2010', -5, 150, 16, 11, 'MG'),
    Volcano('Costa Rica', '16-07-2010', 15, -87, 16, 18, 'MG'),
    Volcano('Miyakejima', '16-07-2010', 35, 140, 16, 8, 'MG'),
    Volcano('Karanget.', '15-08-2010', 3, 125, 16, 17, 'M'),
    Volcano('Nicaragua', '15-08-2010', 15, -85, 16, 17, 'M'),
    Volcano('Van.', '15-08-2010', -16, 168, 16, 9, 'M'),
    Volcano('Galeras', '30-08-2010', 5, -77, 16, 16, 'M'),
    Volcano('Sinabung', '30-08-2010', 5, 100, 16, 20, 'M'),
    Volcano('Karangetang', '04-10-2010', 3, 125, 16, 28, 'M'),
    Volcano('Barren Island', '04-10-2010', 12, 94, 16, 19, 'M'),
    Volcano('Merapi', '08-11-2010', -7, 110, 17, 108, 'M'),
    Volcano('Tengger C.', '23-12-2010', -8, 110, 17, 23, 'M'),
    Volcano('Tungu.', '23-12-2010', -3, -78, 17, 19, 'M'),
    Volcano('Chile', '23-12-2010', -40, -75, 17, 12, 'M'),
    Volcano('Tengger C.', '07-01-2011', -8, 110, 16, 40, 'M'),
    Volcano('Lokon - Empung', '26-02-2011', 1, 125, 16, 19, 'M'),
    Volcano('Planchon', '26-02-2011', -35, -75, 15, 5, 'M'),
    Volcano('Bulusan', '26-02-2011', 13, 125, 16, 17, 'M'),
    Volcano('Karangetang', '23-03-2011', 2, 125, 15, 12, 'M'),
    Volcano('Sangay', '23-03-2011', -2, -78, 15, 12, 'M'),
    Volcano('Planchon', '23-03-2011', -35, -75, 15, 6, 'M'),
    Volcano('Galeras', '12-04-2011', 5, -77, 16, 14, 'M'),
    Volcano('Karangetang', '12-04-2011', 5, 128, 16, 13, 'M'),
    Volcano('Tungurahua', '02-05-2011', 2, -78, 16, 18, 'M'),
    Volcano('Dukono', '02-05-2011', 2, 128, 16, 13, 'M'),
    Volcano('Van.', '02-05-2011', -16, 160, 15, 7, 'M'),
    Volcano('Grimsvötn', '27-05-2011', 65, -20, 14, 20, 'M'),
    Volcano('Lokon', '27-05-2011', 1, 125, 16, 30, 'M'),
    Volcano('Puyehue', '11-06-2011', -41, -71, 13, 23, 'G,'),
    Volcano('Nabro', '21-06-2011', 13, 41, 17, 446, 'MG'),
    Volcano('Soputan', '20-08-2011', 1, 125, 18, 15, 'MG'),
    Volcano('Marapi', '20-08-2011', 0, 100, 16, 5, 'MG'),
    Volcano('Manam', '19-10-2011', -4, 144, 16, 14, 'M'),
    Volcano('Tungurahua', '19-10-2011', -3, -78, 16, 14, 'M'),
    Volcano('Nyamuragira', '18-11-2011', -2, 29, 16, 39, 'M'),
    Volcano('Gamalama', '18-12-2011', 1, 128, 16, 27, 'M'),
    Volcano('Nyamuragira', '18-12-2011', -1, 29, 15, 19, 'M'),
    Volcano('Vanuatu', '12-01-2012', -16, 168, 16, 20, 'M'),
    Volcano('Nyamuragira', '12-01-2012', -1, 29, 14, 17, 'M'),
    Volcano('Vanuatu', '11-02-2012', -16, 168, 17, 23, 'M'),
    Volcano('Nyamuragira', '11-02-2012', -1, 29, 17, 22, 'M'),
    Volcano('N.·Ruiz', '12-03-2012', -3, -76, 16, 17, 'M'),
    Volcano('Marapi', '12-03-2012', 0, 100, 17, 21, 'M'),
    Volcano('Copahue', '23-12-2012', 37.51, -71.1, 10, 500, 'Smithsonian'),
    Volcano('Kelud', '13-02-2014', -7.55, 112, 19, 200, 'Smithsonian'),
    Volcano('Calbuco', '22-04-2015', 41.19, -72.37, 20, 400, 'Smithsonian')]

name = []
date = []
lat = []
lon = []
alt = []
so2 = []
meas_type = []
for volc in volcanoes:
    name.append(volc.name)
    date.append(np.datetime64(volc.date.split('-')[2] + '-'
                              + volc.date.split('-')[1] + '-'
                              + volc.date.split('-')[0]))
    lat.append(volc.latitude)
    lon.append(volc.longitude)
    alt.append(volc.altitude)
    so2.append(volc.so2)
    meas_type.append(volc.measurement)

xr.Dataset({'latitude': (['time'], [v.latitude for v in volcanoes]),
            'longitude': (['time'], [v.longitude for v in volcanoes]),
            'altitude': (['time'], [v.altitude for v in volcanoes]),
            'so2': (['time'], [v.so2 for v in volcanoes]),
            'measurement_type': (['time'], [v.measurement for v in volcanoes])},
           {'time': pd.to_datetime([np.datetime64(v.date.split('-')[2] + '-' +
                                                 v.date.split('-')[1] + '-' +
                                                 v.date.split('-')[0]) for v in volcanoes])}).to_netcdf('volcanoes.nc')
