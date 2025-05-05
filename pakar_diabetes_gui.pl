% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA PENYAKIT
penyakit("Diabetes Melitus Tipe 1").
penyakit("Diabetes Melitus Tipe 2").
penyakit("Diabetes Gestasional").
penyakit("Diabetes Insipidus").

% GEJALA PER PENYAKIT
gejala(sering_buang_air_kecil, "Diabetes Melitus Tipe 1").
gejala(sangat_haus, "Diabetes Melitus Tipe 1").
gejala(berat_badan_turun, "Diabetes Melitus Tipe 1").
gejala(lelah_berlebihan, "Diabetes Melitus Tipe 1").
gejala(penglihatan_kabur, "Diabetes Melitus Tipe 1").

gejala(sering_buang_air_kecil, "Diabetes Melitus Tipe 2").
gejala(sangat_haus, "Diabetes Melitus Tipe 2").
gejala(luka_sulit_sembuh, "Diabetes Melitus Tipe 2").
gejala(kesemutan, "Diabetes Melitus Tipe 2").
gejala(penglihatan_kabur, "Diabetes Melitus Tipe 2").

gejala(sangat_haus, "Diabetes Gestasional").
gejala(sering_buang_air_kecil, "Diabetes Gestasional").
gejala(lelah_berlebihan, "Diabetes Gestasional").

gejala(sering_buang_air_kecil_berlebihan, "Diabetes Insipidus").
gejala(sangat_haus, "Diabetes Insipidus").
gejala(dehidrasi, "Diabetes Insipidus").

% PERTANYAAN
pertanyaan(sering_buang_air_kecil, Y) :-
    Y = "Apakah Anda sering buang air kecil?".

pertanyaan(sangat_haus, Y) :-
    Y = "Apakah Anda merasa sangat haus?".

pertanyaan(berat_badan_turun, Y) :-
    Y = "Apakah berat badan Anda turun drastis tanpa sebab jelas?".

pertanyaan(lelah_berlebihan, Y) :-
    Y = "Apakah Anda merasa sangat lelah/tidak bertenaga?".

pertanyaan(penglihatan_kabur, Y) :-
    Y = "Apakah Anda mengalami penglihatan kabur?".

pertanyaan(luka_sulit_sembuh, Y) :-
    Y = "Apakah luka Anda sulit sembuh?".

pertanyaan(kesemutan, Y) :-
    Y = "Apakah Anda sering mengalami kesemutan pada tangan/kaki?".

pertanyaan(sering_buang_air_kecil_berlebihan, Y) :-
    Y = "Apakah Anda buang air kecil sangat banyak dalam sehari?".

pertanyaan(dehidrasi, Y) :-
    Y = "Apakah Anda sering merasa dehidrasi atau mulut kering?".
