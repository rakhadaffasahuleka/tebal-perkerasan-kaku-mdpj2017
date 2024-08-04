import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import math
import openpyxl
from kumfungsi import *
import numpy as np

PAGE_TITTLE = "Desain Perkerasan Kaku | Itenas"
PAGE_ICON = Image.open('logoitenas.png')
st.set_page_config(page_icon=PAGE_ICON, page_title=PAGE_TITTLE)
# Navigasi Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "Desain Perkerasan Kaku",
        options = ['Home',
                        'Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga MDPJ 2017',
                        'Desain Perkerasan Kaku NIlai VDF Nilai VDF Kendaraan Niaga Berdasarkan Jenis Kendaraan Dan Muatan MDPJ 2017',
                        'Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga Suplemen MDPJ 2017',],
        icons = ["house",],
        default_index=0,
    )

### --------------- HOME ---------------- ###
if (selected == 'Home') :
    def main():
        col1, col2 = st.columns([1,4])
        with col1:
            st.image(PAGE_ICON)
        with col2:
            st.write("<h1 style='font-size: 36px;'>Desain Perkerasan Kaku Dengan Metode Manual Desain Perkerasan Jalan Tahun 2017</h1>", 
                     unsafe_allow_html=True)
        st.write("---")
        st.image('tabel1.png', caption="Nilai VDF Kendaraan Niaga MDPJ 2017")
        st.image('tabel2.png', caption="Nilai VDF Kendaraan Niaga Berdasarkan Jenis Kendaraan Dan Muatan5 MDPJ 2017")
        
        st.write("---")
        st.subheader("Dibuat oleh:")
        st.write("Ir. Kamaludin, M.T., M.Kom.")
        st.write("Dr. Sofyan Triana, S.T., M.T.")
        st.write("Rakha Daffa Sahuleka")
  
    if __name__ == '__main__':
        main()

### ------------- TABEL 1 --------------- ###
if (selected == 'Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga MDPJ 2017') :
    st.title('Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga MDPJ 2017')
    # membuat tabs
    tabs1, tabs2, tabs3, tabs4 = st.tabs(["Input Deskripsi Umum", "Input Data Lalu Lintas Harian", "Menghitung Stabilisasi Tanah", "Menghitung Perkerasan Kaku"])
    ########################## TABS 1 ############################
    with tabs1:
        ## Membagi Kolom
        col1, col2 = st.columns(2)
        # Deskripsi Jalan
        jalan = ['Jalan desa minor dengan akses kendaraan berat terbatas','Jalan kecil dua arah'
                 ,'Jalan lokal','Akses lokal daerah industri atau quarry','Jalan kolektor']
        deskripsi_jalan = st.radio("Deskripsi Jalan", jalan)
        # Daerah
        Daerah_Tabel1 = ['Sumatera', 'Jawa', 'Kalimantan', 'Sulawesi', 'Bali, Nusa Tenggara, Maluku, dan Papua']
        Daerah_tinjauan = st.selectbox("Daerah Yang Ditinjau", Daerah_Tabel1)
        with col1:
            # Faktor Distibusi Lajur
            DL = (st.number_input("Masukkan Nilai Faktor Distribusi Lajur (DL)", value = 0.5))
            # Faktor Distribusi Arah
            DD = st.number_input("Masukkan Nilai Faktor Distribusi Arah (DD)", value = 0.5)
            # Lebar Lajur
            lebar_lajur = (st.number_input ("Lebar Lajur (m)", value = 3.0))
        with col2:
            # Umur Rencana
            UR = (st.number_input ("Masukka Umur Rencana (UR)", min_value=0,value = 40))
            # Faktor Laju Pertumbuhan Lalu Lintas (i)
            i = (st.number_input ("Masukkan Nilai Faktor Laju Pertumbuhan Lalu Lintas (i)", value = 1.0))
        # Faktor Pengali Pertumbuhan Lalu Lintas (R)
        faktor_pengali_pertumbuhan_lalu_lintas = ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i))
        tampil_input_lhr = st.checkbox("Lanjutkan")
    with tabs2:
        if tampil_input_lhr :
            ## Membagi Kolom
            col1, col2, col3 = st.columns(3)
            with col1 :
                st.write("Jenis Kendaraan")
                st.write("2,3,4")
                st.write(" ")
                st.write("5A")
                st.write(" ")
                st.write("5B")
                st.write(" ")
                st.write("6A")
                st.write(" ")
                st.write("6B")
                st.write(" ") 
                st.write("7A1")
                st.write(" ")
                st.write("7A2")
                st.write(" ")
                st.write("7B1")
                st.write(" ")
                st.write("7B2")
                st.write(" ")
                st.write("7C1")
                st.write(" ")
                st.write("7C2A")
                st.write(" ")
                st.write("7C2B")
                st.write("7C3")
            with col2 :
                st.write("Lalu Lintas Harian Rata-Rata")
                lhr234_t1 = st.number_input ("                  ", min_value=0,value = 10, label_visibility="collapsed")
                lhr5A_t1 = st.number_input ("",min_value=0, value = 10, label_visibility="collapsed")
                lhr5B_t1 = st.number_input (" ",0, label_visibility="collapsed")
                lhr6A_t1 = st.number_input ("  ",0, label_visibility="collapsed")
                lhr6B_t1 = st.number_input ("   ",0, label_visibility="collapsed")
                lhr7A1_t1 = st.number_input ("    ",0, label_visibility="collapsed")
                lhr7A2_t1 = st.number_input ("     ",0, label_visibility="collapsed")
                lhr7B1_t1 = st.number_input ("      ",0, label_visibility="collapsed")
                lhr7B2_t1 = st.number_input ("        ",0, label_visibility="collapsed")
                lhr7C1_t1 = st.number_input ("         ",0, label_visibility="collapsed")
                lhr7C2A_t1 = st.number_input ("          ",0, label_visibility="collapsed")
                lhr7C2B_t1 = st.number_input ("           ",0, label_visibility="collapsed")
                lhr7C3_t1 = st.number_input ("            ",0, label_visibility="collapsed")
            jmlkendberat_t1 = (lhr5B_t1 + lhr6A_t1 + lhr6B_t1 + lhr7A1_t1 + lhr7A2_t1
                                        + lhr7B1_t1 + lhr7B2_t1 + lhr7C1_t1 + lhr7C2A_t1 + lhr7C2B_t1 + lhr7C3_t1)
            total_lhr_t1 = (lhr234_t1 + lhr5A_t1 + lhr5B_t1 + lhr6A_t1 + lhr6B_t1 + lhr7A1_t1 + lhr7A2_t1
                            + lhr7B1_t1 + lhr7B2_t1 + lhr7C1_t1 + lhr7C2A_t1 + lhr7C2B_t1 + lhr7C3_t1)
            if Daerah_tinjauan == "Sumatera" :
                # -BEBAN AKTUAL VDF 4- #
                stabilisasi_t1_BA_VDF5_5B = 1
                stabilisasi_t1_BA_VDF5_6A = 0.5
                stabilisasi_t1_BA_VDF5_6B = 7.4
                stabilisasi_t1_BA_VDF5_7A1 = 18.4
                stabilisasi_t1_BA_VDF5_7A2 = 20
                stabilisasi_t1_BA_VDF5_7B1 = 0
                stabilisasi_t1_BA_VDF5_7B2 = 0
                stabilisasi_t1_BA_VDF5_7C1 = 29.5
                stabilisasi_t1_BA_VDF5_7C2A = 39
                stabilisasi_t1_BA_VDF5_7C2B = 42.8
                stabilisasi_t1_BA_VDF5_7C3 = 51.7
            elif Daerah_tinjauan == "Jawa" :
                stabilisasi_t1_BA_VDF5_5B = 1
                stabilisasi_t1_BA_VDF5_6A = 0.5
                stabilisasi_t1_BA_VDF5_6B = 9.2
                stabilisasi_t1_BA_VDF5_7A1 = 14.4
                stabilisasi_t1_BA_VDF5_7A2 = 19
                stabilisasi_t1_BA_VDF5_7B1 = 18.2
                stabilisasi_t1_BA_VDF5_7B2 = 21.8
                stabilisasi_t1_BA_VDF5_7C1 = 19.8
                stabilisasi_t1_BA_VDF5_7C2A = 33
                stabilisasi_t1_BA_VDF5_7C2B = 24.2
                stabilisasi_t1_BA_VDF5_7C3 = 34.4
            elif Daerah_tinjauan == 'Kalimantan' :
                stabilisasi_t1_BA_VDF5_5B = 1
                stabilisasi_t1_BA_VDF5_6A = 0.5
                stabilisasi_t1_BA_VDF5_6B = 8.5
                stabilisasi_t1_BA_VDF5_7A1 = 18.3
                stabilisasi_t1_BA_VDF5_7A2 = 17.7
                stabilisasi_t1_BA_VDF5_7B1 = 0
                stabilisasi_t1_BA_VDF5_7B2 = 0
                stabilisasi_t1_BA_VDF5_7C1 = 20.4
                stabilisasi_t1_BA_VDF5_7C2A = 14.7
                stabilisasi_t1_BA_VDF5_7C2B = 0
                stabilisasi_t1_BA_VDF5_7C3 = 22.9
            elif Daerah_tinjauan == 'Sulawesi' :
                stabilisasi_t1_BA_VDF5_5B = 1
                stabilisasi_t1_BA_VDF5_6A = 0.5
                stabilisasi_t1_BA_VDF5_6B = 9
                stabilisasi_t1_BA_VDF5_7A1 = 11.4
                stabilisasi_t1_BA_VDF5_7A2 = 19.1
                stabilisasi_t1_BA_VDF5_7B1 = 0
                stabilisasi_t1_BA_VDF5_7B2 = 0
                stabilisasi_t1_BA_VDF5_7C1 = 25.5
                stabilisasi_t1_BA_VDF5_7C2A = 42
                stabilisasi_t1_BA_VDF5_7C2B = 28.8
                stabilisasi_t1_BA_VDF5_7C3 = 59.6
            elif Daerah_tinjauan == 'Bali, Nusa Tenggara, Maluku, dan Papua' :
                stabilisasi_t1_BA_VDF5_5B = 1
                stabilisasi_t1_BA_VDF5_6A = 0.5
                stabilisasi_t1_BA_VDF5_6B = 4
                stabilisasi_t1_BA_VDF5_7A1 = 0
                stabilisasi_t1_BA_VDF5_7A2 = 9.7
                stabilisasi_t1_BA_VDF5_7B1 = 0
                stabilisasi_t1_BA_VDF5_7B2 = 0
                stabilisasi_t1_BA_VDF5_7C1 = 11.9
                stabilisasi_t1_BA_VDF5_7C2A = 0
                stabilisasi_t1_BA_VDF5_7C2B = 0
                stabilisasi_t1_BA_VDF5_7C3 = 0
            # -BEBAN LALU LINTAS DESAIN- #
            esa_stabilisasi_t1_234 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr234_t1 * 0 *0.5)
            esa_stabilisasi_t1_5A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr5A_t1 * 0 *0.5)
            esa_stabilisasi_t1_5B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr5B_t1 * stabilisasi_t1_BA_VDF5_5B *0.5)
            esa_stabilisasi_t1_6A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr6A_t1 * stabilisasi_t1_BA_VDF5_6A *0.5)
            esa_stabilisasi_t1_6B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr6B_t1 * stabilisasi_t1_BA_VDF5_6B *0.5)
            esa_stabilisasi_t1_7A1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7A1_t1 * stabilisasi_t1_BA_VDF5_7A1 *0.5)
            esa_stabilisasi_t1_7A2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7A2_t1 * stabilisasi_t1_BA_VDF5_7A2 *0.5)
            esa_stabilisasi_t1_7B1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7B1_t1 * stabilisasi_t1_BA_VDF5_7B1 *0.5)
            esa_stabilisasi_t1_7B2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7B2_t1 * stabilisasi_t1_BA_VDF5_7B2 *0.5)
            esa_stabilisasi_t1_7C1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C1_t1 * stabilisasi_t1_BA_VDF5_7C1 *0.5)
            esa_stabilisasi_t1_7C2A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C2A_t1 * stabilisasi_t1_BA_VDF5_7C2A *0.5)
            esa_stabilisasi_t1_7C2B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C2B_t1 * stabilisasi_t1_BA_VDF5_7C2B *0.5)
            esa_stabilisasi_t1_7C3 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C3_t1 * stabilisasi_t1_BA_VDF5_7C3 *0.5)
            cesa4_stabilisasi_t1 = (esa_stabilisasi_t1_5B + esa_stabilisasi_t1_6A
                                            + esa_stabilisasi_t1_6B + esa_stabilisasi_t1_7A1
                                            + esa_stabilisasi_t1_7A2 + esa_stabilisasi_t1_7B1
                                            + esa_stabilisasi_t1_7B2 + esa_stabilisasi_t1_7C1
                                            + esa_stabilisasi_t1_7C2A + esa_stabilisasi_t1_7C2B
                                            + esa_stabilisasi_t1_7C3)
            tampil_input_cbrt1 = st.checkbox("Input Data CBR")
    
            with tabs3:
                if tampil_input_cbrt1 :
                    st.write("Format file excel harus sesuai dengan template yang telah disediakan berikut")
                    with open("template.xlsx", "rb") as file:
                        btn = st.download_button(
                                label="Download File Excel",
                                data=file,
                                file_name="template.xlsx",
                                mime="xlsx")

                    ## ------ UPLOAD FILE EXCEL
                    upload_file_excel = st.file_uploader('Masukkan Data CBR Dalam Format xlsx', type='xlsx')
                    if upload_file_excel :
                        st.markdown('---')
                        df = pd.read_excel(upload_file_excel, engine='openpyxl')
                        st.write("Data awal :")
                        st.dataframe(df)
                        staberapa = df['STA']
                        nilaicbr = df['NILAI CBR']
                        koefvar=fkoefvar(df)
                        rata2=df["NILAI CBR"].mean()
                        nstd=df["NILAI CBR"].std()
                        jumlahdata=len(df)
                        df_data_awal = pd.DataFrame(
                                        {
                                            "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi"],
                                            "Hasil" : [(jumlahdata), (rata2), (nstd), (koefvar)]
                                        }
                                    )
                        st.dataframe(df_data_awal)
                        if (koefvar < 30) or (jumlahdata <=10):
                            st.success("Dapat dijadikan satu segemen")
                        else :
                            st.warning("Tidak dapat dijadikan satu segemen")
                        
                        rumus_cbr_karakteristik = st.selectbox("Rumus CBR Karakteristik",['Metode distribusi normal standar',
                                                                                        'Metode persentil',])
                        if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                            pilih_tipe_jalan = st.radio("Tipe Jalan",['Bebas Hambatan', 'Jalan Kolektor atau Arteri', 'Jalan Lokal dan Jalan Kecil'])
                            if pilih_tipe_jalan == 'Jalan Kolektor atau Arteri':
                                f_nilai = 1.282
                            elif pilih_tipe_jalan == 'Bebas Hambatan':
                                f_nilai = 1.645
                            elif pilih_tipe_jalan == 'Jalan Lokal dan Jalan Kecil':
                                f_nilai = 0.842

                        jumlah_segmen = int(st.number_input("Input jumlah segmen :",1))
                        # List untuk menyimpan jumlah data per list yang diinput oleh pengguna
                        data_per_list = []
                        # Memasukkan jumlah data per list sesuai jumlah list yang diinginkan
                        ukuran_bagian=(jumlahdata//jumlah_segmen)
                        junlahdataterambil=ukuran_bagian*jumlah_segmen
                        bagian = []
                        startdata = 0
                        for i in range(jumlah_segmen-1):
                            enddata = min(startdata + ukuran_bagian, jumlahdata)
                            bagian.append(df.iloc[startdata:enddata])
                            startdata=enddata
                        bagian.append(df.iloc[startdata:jumlahdata])
                        statussegmen=False
                        for i in range(jumlah_segmen):
                            jml_data_persegmen = len(bagian[i])
                            data = st.number_input(f"Masukkan banyak data CBR untuk segmen {i+1}", min_value=1, value=jml_data_persegmen)
                            data_per_list.append(data)

                        # Memunculkan hasil pembagian data pada list
                        if st.button("Tampilkan"):
                            if len(df) > 0:
                                lists = divide_into_lists(df, data_per_list)
                                for i, lst in enumerate(lists, start=1):
                                    jumlah_banyak_data_cbr = len(lst)
                                    st.write(f"Segmen ke-{i} dengan jumlah data {jumlah_banyak_data_cbr} dapat dilihat pada tabel berikut :")
                                    st.dataframe(lst)
                                    Nilai_cbr_rata2 = cbr_rata2(lst)
                                    nilai_devstandar = nilai_std(lst)
                                    koefvar=fkoefvar(lst)
                                    if len(lst)>10 and koefvar>30:
                                        statussegmen=True
                                    else :
                                        statussegmen=False
                                    if jumlah_banyak_data_cbr < 10:
                                        nilai_terkecil_cbr = min((lst["NILAI CBR"]))
                                        cbr_karakteristik = nilai_terkecil_cbr
                                    else :
                                        if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                                            cbr_karakteristik = Nilai_cbr_rata2 - f_nilai * nilai_devstandar
                                        else :
                                            xdata=(lst["NILAI CBR"])
                                            cbr_karakteristik = np.percentile(xdata, 10)
                                    ## -STABILISASI TANAH
                                    if  cbr_karakteristik < 1:
                                        nilai_stabilisasi = "Perlu penangan lebih lanjut"
                                    elif  1 <= cbr_karakteristik < 2.5:
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = 1000
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = 1100
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = 1200
                                    elif  2.5 <= cbr_karakteristik < 3:
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = 175
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = 250
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = 350
                                    elif 3 <= cbr_karakteristik < 4 :
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = 150
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = 200
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = 300
                                    elif 4 <= cbr_karakteristik < 5 :
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = 100
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = 150
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = 200
                                    elif 5 <= cbr_karakteristik < 6 :
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = 100
                                    elif cbr_karakteristik >= 6 :
                                        if cesa4_stabilisasi_t1 < 2000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif 2000000 <= cesa4_stabilisasi_t1 <= 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif cesa4_stabilisasi_t1 > 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                    ## --TABEL HASIL
                                    df_hasil_stabilisasi = pd.DataFrame(
                                        {
                                            "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi", "CBR Karakteristik",
                                                      "Beban lalu lintas pada lajur rencana dengan umur rencana 40 tahun (juta ESA5)" ,
                                                      "Tebal Minimum Material Timbunan Pilihan (mm)", "Stabilisasi Diatas Material Timbunan Pilihan (mm)"],
                                            "Hasil" : [(jumlah_banyak_data_cbr), round(Nilai_cbr_rata2, 3), round(nilai_devstandar, 3), round(koefvar, 3), 
                                                    round(cbr_karakteristik, 3), (cesa4_stabilisasi_t1), (nilai_stabilisasi), ("150")]
                                        }
                                    )
                                    st.dataframe(df_hasil_stabilisasi)
                                    # st.warning(koefvar)
                                    if statussegmen:
                                        st.warning("Sebaiknya dibagi segmen lagi")
                                    else:
                                        st.success(f"Segmen {i} memenuhi")


                    with tabs4:
                        if tampil_input_lhr :
                            st.write('Untuk dapat mengeluarkan hasil tebal perkerasan dapat menekan tombol "Hasil" dibawah ini.')
                            HASIL_t1 = st.checkbox ("Hasil")
                            if HASIL_t1 :
                                if Daerah_tinjauan == 'Sumatera' :
                                    # -----BEBAN AKTUAL VDF 4- #
                                    t1_BA_VDF4_5B = 1
                                    t1_BA_VDF4_6A = 0.55
                                    t1_BA_VDF4_6B = 4.5
                                    t1_BA_VDF4_7A1 = 10.1
                                    t1_BA_VDF4_7A2 = 10.5
                                    t1_BA_VDF4_7B1 = 0
                                    t1_BA_VDF4_7B2 = 0
                                    t1_BA_VDF4_7C1 = 15.9
                                    t1_BA_VDF4_7C2A = 19.8
                                    t1_BA_VDF4_7C2B = 20.7
                                    t1_BA_VDF4_7C3 = 24.5
                                elif Daerah_tinjauan == 'Jawa' :
                                    # ------BEBAN AKTUAL VDF 4- #
                                    t1_BA_VDF4_5B = 1
                                    t1_BA_VDF4_6A = 0.55
                                    t1_BA_VDF4_6B = 5.3
                                    t1_BA_VDF4_7A1 = 8.2
                                    t1_BA_VDF4_7A2 = 10.2
                                    t1_BA_VDF4_7B1 = 11.8
                                    t1_BA_VDF4_7B2 = 13.7
                                    t1_BA_VDF4_7C1 = 11
                                    t1_BA_VDF4_7C2A = 17.7
                                    t1_BA_VDF4_7C2B = 13.4
                                    t1_BA_VDF4_7C3 = 18.1                    
                                elif Daerah_tinjauan == 'Kalimantan' :
                                    # -BEBAN AKTUAL VDF 4- #
                                    t1_BA_VDF4_5B = 1
                                    t1_BA_VDF4_6A = 0.55
                                    t1_BA_VDF4_6B = 4.8
                                    t1_BA_VDF4_7A1 = 9.9
                                    t1_BA_VDF4_7A2 = 9.6
                                    t1_BA_VDF4_7B1 = 0
                                    t1_BA_VDF4_7B2 = 0
                                    t1_BA_VDF4_7C1 = 11.7
                                    t1_BA_VDF4_7C2A = 8.2
                                    t1_BA_VDF4_7C2B = 0
                                    t1_BA_VDF4_7C3 = 13.5                   
                                ### --------- SULAWESI BEBAN LALU LINTAS DESAIN VDF 4 DAN VDF 5 ---------- ###
                                elif Daerah_tinjauan == 'Sulawesi' :
                                    # -BEBAN AKTUAL VDF 4- #
                                    t1_BA_VDF4_5B = 1
                                    t1_BA_VDF4_6A = 0.55
                                    t1_BA_VDF4_6B = 4.9
                                    t1_BA_VDF4_7A1 = 7.2
                                    t1_BA_VDF4_7A2 = 9.4
                                    t1_BA_VDF4_7B1 = 0
                                    t1_BA_VDF4_7B2 = 0
                                    t1_BA_VDF4_7C1 = 13.2
                                    t1_BA_VDF4_7C2A = 20.2
                                    t1_BA_VDF4_7C2B = 17
                                    t1_BA_VDF4_7C3 = 28.7
                                ### --------- BALI,NUSA TENGGARA,MALUKU,PAPUA BEBAN LALU LINTAS DESAIN VDF 4 DAN VDF 5 ---------- ###
                                elif Daerah_tinjauan == 'Bali, Nusa Tenggara, Maluku, dan Papua' :
                                    # -BEBAN AKTUAL VDF 4- #
                                    t1_BA_VDF4_5B = 1
                                    t1_BA_VDF4_6A = 0.55
                                    t1_BA_VDF4_6B = 3
                                    t1_BA_VDF4_7A1 = 0
                                    t1_BA_VDF4_7A2 = 4.9
                                    t1_BA_VDF4_7B1 = 0
                                    t1_BA_VDF4_7B2 = 0
                                    t1_BA_VDF4_7C1 = 8
                                    t1_BA_VDF4_7C2A = 0
                                    t1_BA_VDF4_7C2B = 0
                                    t1_BA_VDF4_7C3 = 0
                                def e1p_t1() :
                                    # -BEBAN LALU LINTAS DESAIN- #
                                    e1p_t1__234 = math.ceil(365 * 22 * lhr234_t1 * 0 * 0.5)
                                    e1p_t1__5A = math.ceil(365 * 22 * lhr5A_t1 * 0 * 0.5)
                                    e1p_t1__5B = math.ceil(365 * 22 * lhr5B_t1 * t1_BA_VDF4_5B * 0.5)
                                    e1p_t1__6A = math.ceil(365 * 22 * lhr6A_t1 * t1_BA_VDF4_6A * 0.5)
                                    e1p_t1__6B = math.ceil(365 * 22 * lhr6B_t1 * t1_BA_VDF4_6B * 0.5)
                                    e1p_t1__7A1 = math.ceil(365 * 22 * lhr7A1_t1 * t1_BA_VDF4_7A1 * 0.5)
                                    e1p_t1__7A2 = math.ceil(365 * 22 * lhr7A2_t1 * t1_BA_VDF4_7A2 * 0.5)
                                    e1p_t1__7B1 = math.ceil(365 * 22 * lhr7B1_t1 * t1_BA_VDF4_7B1 * 0.5)
                                    e1p_t1__7B2 = math.ceil(365 * 22 * lhr7B2_t1 * t1_BA_VDF4_7B2 * 0.5)
                                    e1p_t1__7C1 = math.ceil(365 * 22 * lhr7C1_t1 * t1_BA_VDF4_7C1 * 0.5)
                                    e1p_t1__7C2A = math.ceil(365 * 22 * lhr7C2A_t1 * t1_BA_VDF4_7C2A * 0.5)
                                    e1p_t1__7C2B = math.ceil(365 * 22 * lhr7C2B_t1 * t1_BA_VDF4_7C2B * 0.5)
                                    e1p_t1__7C3 = math.ceil(365 * 22 * lhr7C3_t1 * t1_BA_VDF4_7C3 * 0.5)
                                    cesa4_e1p_t1 = (e1p_t1__234 + e1p_t1__5A + e1p_t1__5B
                                                                    + e1p_t1__6A + e1p_t1__6B + e1p_t1__7A1
                                                                    + e1p_t1__7A2 + e1p_t1__7B1 + e1p_t1__7B2
                                                                    + e1p_t1__7C1 + e1p_t1__7C2A + e1p_t1__7C2B
                                                                    + e1p_t1__7C3)
                                    return cesa4_e1p_t1
                                def e3p_t1() :
                                    # -BEBAN LALU LINTAS DESAIN- #
                                    e3p_t1__234 = math.ceil(365 * 28.2 * lhr234_t1 * 0 * 0.5)
                                    e3p_t1__5A = math.ceil(365 * 28.2 * lhr5A_t1 * 0 * 0.5)
                                    e3p_t1__5B = math.ceil(365 * 28.2 * lhr5B_t1 * t1_BA_VDF4_5B * 0.5)
                                    e3p_t1__6A = math.ceil(365 * 28.2 * lhr6A_t1 * t1_BA_VDF4_6A * 0.5)
                                    e3p_t1__6B = math.ceil(365 * 28.2 * lhr6B_t1 * t1_BA_VDF4_6B * 0.5)
                                    e3p_t1__7A1 = math.ceil(365 * 28.2 * lhr7A1_t1 * t1_BA_VDF4_7A1 * 0.5)
                                    e3p_t1__7A2 = math.ceil(365 * 28.2 * lhr7A2_t1 * t1_BA_VDF4_7A2 * 0.5)
                                    e3p_t1__7B1 = math.ceil(365 * 28.2 * lhr7B1_t1 * t1_BA_VDF4_7B1 * 0.5)
                                    e3p_t1__7B2 = math.ceil(365 * 28.2 * lhr7B2_t1 * t1_BA_VDF4_7B2 * 0.5)
                                    e3p_t1__7C1 = math.ceil(365 * 28.2 * lhr7C1_t1 * t1_BA_VDF4_7C1 * 0.5)
                                    e3p_t1__7C2A = math.ceil(365 * 28.2 * lhr7C2A_t1 * t1_BA_VDF4_7C2A * 0.5)
                                    e3p_t1__7C2B = math.ceil(365 * 28.2 * lhr7C2B_t1 * t1_BA_VDF4_7C2B * 0.5)
                                    e3p_t1__7C3 = math.ceil(365 * 28.2 * lhr7C3_t1 * t1_BA_VDF4_7C3 * 0.5)
                                    cesa4_e3p_t1 = math.ceil(e3p_t1__234 + e3p_t1__5A + e3p_t1__5B
                                                                    + e3p_t1__6A + e3p_t1__6B + e3p_t1__7A1
                                                                    + e3p_t1__7A2 + e3p_t1__7B1 + e3p_t1__7B2
                                                                    + e3p_t1__7C1 + e3p_t1__7C2A + e3p_t1__7C2B
                                                                    + e3p_t1__7C3)
                                    return cesa4_e3p_t1
                                
                                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas'  :
                                    beban_lalin_t1 = e1p_t1()
                                elif deskripsi_jalan == 'Jalan kecil dua arah':
                                    beban_lalin_t1 = e1p_t1()
                                elif deskripsi_jalan == 'Jalan lokal':
                                    beban_lalin_t1 = e1p_t1()
                                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry': 
                                    beban_lalin_t1 = e3p_t1()
                                elif deskripsi_jalan =='Jalan kolektor' :
                                    beban_lalin_t1 = e3p_t1()
                                
                                # -BEBAN LALU LINTAS DESAIN- #
                                esa_lalinberat_t1__234 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr234_t1 * 0 * DD)
                                esa_lalinberat_t1__5A = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr5A_t1 * 0 * DD)
                                esa_lalinberat_t1__5B = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr5B_t1 * 2 * DD)
                                esa_lalinberat_t1__6A = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr6A_t1 * 2 * DD)
                                esa_lalinberat_t1__6B = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr6B_t1 * 2 * DD)
                                esa_lalinberat_t1__7A1 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7A1_t1 * 2 * DD)
                                esa_lalinberat_t1__7A2 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7A2_t1 * 2 * DD)
                                esa_lalinberat_t1__7B1 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7B1_t1 * 4 * DD)
                                esa_lalinberat_t1__7B2 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7B2_t1 * 4 * DD)
                                esa_lalinberat_t1__7C1 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7C1_t1 * 3 * DD)
                                esa_lalinberat_t1__7C2A = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7C2A_t1 * 3 * DD)
                                esa_lalinberat_t1__7C2B = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7C2B_t1 * 3 * DD)
                                esa_lalinberat_t1__7C3 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * lhr7C3_t1 * 3 * DD)
                                cesa_lalinberat_t1 = math.ceil(esa_lalinberat_t1__234 + esa_lalinberat_t1__5A + esa_lalinberat_t1__5B
                                                    + esa_lalinberat_t1__6A + esa_lalinberat_t1__6B + esa_lalinberat_t1__7A1
                                                    + esa_lalinberat_t1__7A2 + esa_lalinberat_t1__7B1 + esa_lalinberat_t1__7B2
                                                    + esa_lalinberat_t1__7C1 + esa_lalinberat_t1__7C2A + esa_lalinberat_t1__7C2B
                                                    + esa_lalinberat_t1__7C3)
                                # Perencanaan Tebal Perkerasan Lalu
                                if cesa_lalinberat_t1 < 4300000 :
                                    LB_Tebal_Perkerasan_Beton_t1 = 265
                                elif 4300000 <= cesa_lalinberat_t1 < 8600000 :
                                    LB_Tebal_Perkerasan_Beton_t1 = 275
                                elif 8600000 <= cesa_lalinberat_t1 < 25800000 :
                                    LB_Tebal_Perkerasan_Beton_t1 = 285
                                elif 25800000 <= cesa_lalinberat_t1 < 43000000 :
                                    LB_Tebal_Perkerasan_Beton_t1 = 295
                                elif cesa_lalinberat_t1 >= 43000000 :
                                    LB_Tebal_Perkerasan_Beton_t1 = 305
                                def diamater_dowel_t1() :
                                    if 265 <= LB_Tebal_Perkerasan_Beton_t1 <= 275 :
                                        d_dowel = 32
                                        return d_dowel
                                    elif 285 <= LB_Tebal_Perkerasan_Beton_t1 <= 305 :
                                        d_dowel = 40
                                        return d_dowel
                                def diamater_tiebar_t1() :
                                    luas_penampang_tulangan = 204 * (LB_Tebal_Perkerasan_Beton_t1 / 1000) * lebar_lajur
                                    if luas_penampang_tulangan <= 201 :
                                        diamater_tiebar = 16
                                        return diamater_tiebar
                                    elif 201 < luas_penampang_tulangan <= 284 :
                                        diamater_tiebar = 19
                                        return diamater_tiebar
                                    elif 284 < luas_penampang_tulangan <= 380 :
                                        diamater_tiebar = 22
                                        return diamater_tiebar
                                    elif 380 < luas_penampang_tulangan <= 491 :
                                        diamater_tiebar = 25
                                        return diamater_tiebar
                                    elif 491 < luas_penampang_tulangan <= 661 :
                                        diamater_tiebar = 29
                                        return diamater_tiebar
                                    elif 661 < luas_penampang_tulangan <= 804 :
                                        diamater_tiebar = 32
                                        return diamater_tiebar
                                    elif 804 < luas_penampang_tulangan <= 1018 :
                                        diamater_tiebar = 36
                                        return diamater_tiebar
                                    elif 1018 < luas_penampang_tulangan <= 1257 :
                                        diamater_tiebar = 40
                                        return diamater_tiebar
                                    elif 1257 < luas_penampang_tulangan <= 1964 :
                                        diamater_tiebar = 50
                                        return diamater_tiebar
                                    elif 1964 < luas_penampang_tulangan <= 2290 :
                                        diamater_tiebar = 54
                                        return diamater_tiebar
                                    elif 2290 < luas_penampang_tulangan <= 2552 :
                                        diamater_tiebar = 57
                                        return diamater_tiebar
                                d_tiebar = diamater_tiebar_t1()
                                def panjang_batang_pengikat_t1() :
                                    panjang_batang_pengikat = (38.3 * diamater_tiebar_t1()) + 75
                                    return panjang_batang_pengikat

                                def lalin_berat_t1() :    
                                    df_tebal_perkerasan = pd.DataFrame(
                                        {
                                            "Parameter" : [
                                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)", "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                                "Lalu Lintas (Berat/Rendah)", "Komulatif Kelompok Sumbu Kendaraan Berat", "Menggunakan Bahu Pelat Beton",
                                                "Tebal Perkerasan Beton (mm)", "Diameter Dowel (mm)" , "Panjang Dowel (mm)", "Jarak Antar Dowel (mm)",
                                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "Lapis Fondasi LMC (mm)",
                                                "Lapis Dainase (mm)"
                                            ],
                                            "Hasil" : [
                                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr_t1), (beban_lalin_t1), ("Berat"),
                                                (cesa_lalinberat_t1), 
                                                ("Ya"), (LB_Tebal_Perkerasan_Beton_t1), (diamater_dowel_t1()), ("450"), ("300"),
                                                (diamater_tiebar_t1()), round(panjang_batang_pengikat_t1(), 3), ("750"),("100"), ("150")
                                            ]
                                        }
                                    )
                                    return st.dataframe(df_tebal_perkerasan)   
                                    
                                def lalin_rendah_t1() :
                                    keadaan_tanah_dasar = st.selectbox("Tanah Dasar",['Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton',
                                                                                'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton',
                                                                                'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton',
                                                                                'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton'])
                                    if keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton' :
                                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                                        bahu_jalan = "Ya"
                                        tulangan_distribusi_retak = "Ya"
                                        if jmlkendberat_t1 == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat_t1 > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah= 180
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton' :
                                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                                        bahu_jalan = "Tidak"
                                        tulangan_distribusi_retak = "Ya"
                                        if jmlkendberat_t1 == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat_t1 > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 200
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton' :
                                        tanah_dasar = "Dipadatkan Normal"
                                        bahu_jalan = "Ya"
                                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                                        if jmlkendberat_t1 == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 135
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat_t1 > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton' :
                                        tanah_dasar = "Dipadatkan Normal"
                                        bahu_jalan = "Tidak"
                                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                                        if jmlkendberat_t1 == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 150
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat_t1 > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                                            dapat_dilalui_truk = "Ya"
                                    df_tebal_perkerasan = pd.DataFrame(
                                        {
                                            "Parameter" : [
                                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)",
                                                "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                                "Lalu Lintas (Berat/Rendah)", "Tanah Dasar", "Menggunakan Bahu Pelat Beton", "Dapat Dilalui Truk",
                                                "Tebal Perkerasan Beton (mm)", "Tulangan Distribusi Retak", "Dowel" ,
                                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "LMC (mm)",
                                                "Lapis Fondasi Kelas A (Ukuran Butir Nominal Maksimum 30 mm) (mm)", "Jarak Sambungan Melintang (m)"
                                            ],
                                            "Hasil" : [
                                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr_t1), (beban_lalin_t1), ("Rendah"), 
                                                (tanah_dasar), (bahu_jalan), (dapat_dilalui_truk),
                                                (LR_Tebal_Perkerasan_Beton_Rendah), (tulangan_distribusi_retak), ("Tidak Dibutuhkan"), 
                                                (diamater_tiebar_t1()), (panjang_batang_pengikat_t1()), ("750"), ("Tidak Dibutuhkan"),
                                                ("125"), ("4")
                                            ]
                                        }
                                    )
                                    return st.dataframe(df_tebal_perkerasan)
                                beban_lalin_cesa4_e1p = e1p_t1()
                                beban_lalin_cesa4_e3p = e3p_t1()
                                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas' :
                                    if beban_lalin_cesa4_e1p > 45000 :
                                        lalin_berat_t1()
                                    else :
                                        lalin_rendah_t1()
                                elif deskripsi_jalan == 'Jalan kecil dua arah' :
                                    if beban_lalin_cesa4_e1p > 70000 :
                                        lalin_berat_t1()
                                    else :
                                        lalin_rendah_t1()
                                elif deskripsi_jalan == 'Jalan lokal' :
                                    if beban_lalin_cesa4_e1p > 800000 :
                                        lalin_berat_t1()
                                    else :
                                        lalin_rendah_t1()
                                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry' :
                                    if beban_lalin_cesa4_e3p > 1500000 :
                                        lalin_berat_t1()
                                    else :
                                        lalin_rendah_t1()
                                elif deskripsi_jalan == 'Jalan kolektor' :
                                    if beban_lalin_cesa4_e3p > 5000000 :
                                        lalin_berat_t1()
                                    else :
                                        lalin_rendah_t1()

### ------------- TABEL 2 --------------- ###
if (selected == 'Desain Perkerasan Kaku NIlai VDF Nilai VDF Kendaraan Niaga Berdasarkan Jenis Kendaraan Dan Muatan MDPJ 2017') :
    st.title('Desain Perkerasan Kaku NIlai VDF Nilai VDF Kendaraan Niaga Berdasarkan Jenis Kendaraan Dan Muatan MDPJ 2017')
    # membuat tabs
    tabs1, tabs2, tabs3, tabs4 = st.tabs(["Input Deskripsi Umum", "Input Data Lalu Lintas Harian", "Menghitung Stabilisasi Tanah", "Menghitung Perkerasan Kaku" ])
    ########################## TABS 1 ############################
    with tabs1:
        ## Membagi Kolom
        col1, col2 = st.columns(2)
        # Deskripsi Jalan
        jalan = ['Jalan desa minor dengan akses kendaraan berat terbatas','Jalan kecil dua arah'
                 ,'Jalan lokal','Akses lokal daerah industri atau quarry','Jalan kolektor']
        deskripsi_jalan = st.radio("Deskripsi Jalan", jalan)
        with col1:
            # Faktor Distibusi Lajur
            DL = (st.number_input("Masukkan Nilai Faktor Distribusi Lajur (DL)", value = 0.5))
            # Faktor Distribusi Arah
            DD = st.number_input("Masukkan Nilai Faktor Distribusi Arah (DD)", value = 0.5)
            # Lebar Lajur
            lebar_lajur = (st.number_input ("Lebar Lajur (m)", value = 3.0))
        with col2:
            # Umur Rencana
            UR = (st.number_input ("Masukka Umur Rencana (UR)" ,min_value=0,value = 40))
            # Faktor Laju Pertumbuhan Lalu Lintas (i)
            i = (st.number_input ("Masukkan Nilai Faktor Laju Pertumbuhan Lalu Lintas (i)", value = 1.0))
        # Faktor Pengali Pertumbuhan Lalu Lintas (R)
        faktor_pengali_pertumbuhan_lalu_lintas = ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i))
        tampil_input_lhr = st.checkbox("Lanjutkan")
    
    ######################### TABS 2 #################################
    with tabs2:
        if tampil_input_lhr :
            # JALAN DESA MINOR DENGAN AKSES KENDARAAN BERAT TERBATAS #
            ## VDF4 Tabel 4.5 MDPJ 2017
            t2_vdf4sepeda_motor = 0
            t2_vdf4mobil_penumpang = 0
            t2_vdf4bus_kecil = 0.3
            t2_vdf4bus_besar = 1
            t2_vdf4truk2sumbu_cargoringan = 0.3
            t2_vdf4truk2sumbu_ringan = 0.8
            t2_vdf4truk2sumbu_cargosedang = 0.7
            t2_vdf4truk2sumbu_sedang = 1.6
            t2_vdf4truk2sumbu_berat1 = 0.9
            t2_vdf4truk2sumbu_berat2 = 7.3
            t2_vdf4truk3sumbu_ringan = 7.6
            t2_vdf4truk3sumbu_sedang = 28.1
            t2_vdf4truk3sumbu_berat = 28.9
            t2_vdf4truk2sumbu_dan_trailerpenarik2sumbu = 36.9
            t2_vdf4truk4sumbu_trailer = 13.6
            t2_vdf4truk5sumbu_trailer1 = 19
            t2_vdf4truk5sumbu_trailer2 = 30.3
            t2_vdf4truk6sumbu_trailer = 41.6

            ## VDF5 Tabel 4.5 MDPJ 2017
            t2_vdf5sepeda_motor = 0
            t2_vdf5mobil_penumpang = 0
            t2_vdf5bus_kecil = 0.2
            t2_vdf5bus_besar = 1
            t2_vdf5truk2sumbu_cargoringan = 0.2
            t2_vdf5truk2sumbu_ringan = 0.8
            t2_vdf5truk2sumbu_cargosedang = 0.7
            t2_vdf5truk2sumbu_sedang = 1.7
            t2_vdf5truk2sumbu_berat1 = 0.8
            t2_vdf5truk2sumbu_berat2 = 11.2
            t2_vdf5truk3sumbu_ringan = 11.2
            t2_vdf5truk3sumbu_sedang = 64.4
            t2_vdf5truk3sumbu_berat = 62.2
            t2_vdf5truk2sumbu_dan_trailerpenarik2sumbu = 90.4
            t2_vdf5truk4sumbu_trailer = 24
            t2_vdf5truk5sumbu_trailer1 = 33.2
            t2_vdf5truk5sumbu_trailer2 = 69.7
            t2_vdf5truk6sumbu_trailer = 93.7

            ## Membagi Kolom
            col1, col2, col3 = st.columns(3)
            with col1 :
                st.write("Jenis Kendaraan")
                st.write("Sepeda Motor")
                st.write(" ")
                st.write("Mobil Penumpang")
                st.write(" ")
                st.write("Bis Kecil")
                st.write(" ")
                st.write("Bis Besar")
                st.write(" ")
                st.write("Trusk 2 Sumbu -  cargo Ringan")
                st.write(" ") 
                st.write("Truk 2 Sumbu - Ringan")
                st.write(" ")
                st.write("Truk 2 Sumbu - Cargo Sedang")
                st.write(" ")
                st.write("Truk 2 Sumbu - Sedang")
                st.write(" ")
                st.write("Truk 2 Sumbu - Berat (6b2.1)")
                st.write(" ")
                st.write("Truk 2 Sumbu - Berat (6b2.2)")
                st.write(" ")
                st.write("Truk 3 Sumbu - Ringan")
                st.write(" ")
                st.write("Truk 3 Sumbu - Sedang")
                st.write(" ")
                st.write("Truk 3 Sumbu - Berat")
                st.write("Truk 2 Sumbu dan Trailer Penarik 2 Sumbu")
                st.write("Truk 4 Sumbu - Trailer")
                st.write(" ")
                st.write("Truk 5 Sumbu - Trailer (7c2.1)")
                st.write(" ")
                st.write("Truk 5 Sumbu - Trailer (7c2.2)")
                st.write("Truk 6 Sumbu - Trailer")
                            
            with col2 :
                st.write("Lalu Lintas Harian Rata-Rata")
                lhrsepeda_motor = st.number_input ("                  ", min_value=0, value = 10, label_visibility="collapsed")
                lhrmobil_penumpang = st.number_input ("",min_value=0,value = 10, label_visibility="collapsed")
                lhrbus_kecil = st.number_input (" ",0, label_visibility="collapsed")
                lhrbus_besar = st.number_input ("  ",0, label_visibility="collapsed")
                lhrtruk2sumbu_cargoringan = st.number_input ("   ",0, label_visibility="collapsed")
                lhrtruk2sumbu_ringan = st.number_input ("    ",0, label_visibility="collapsed")
                lhrtruk2sumbu_cargosedang = st.number_input ("     ",0, label_visibility="collapsed")
                lhrtruk2sumbu_sedang = st.number_input ("      ",0, label_visibility="collapsed")
                lhrtruk2sumbu_berat1 = st.number_input ("        ",0, label_visibility="collapsed")
                lhrtruk2sumbu_berat2 = st.number_input ("         ",0, label_visibility="collapsed")
                lhrtruk3sumbu_ringan = st.number_input ("          ",0, label_visibility="collapsed")
                lhrtruk3sumbu_sedang = st.number_input ("           ",0, label_visibility="collapsed")
                lhrtruk3sumbu_berat = st.number_input ("            ",0, label_visibility="collapsed")
                lhrtruk2sumbu_dan_trailerpenarik2sumbu = st.number_input ("             ",0, label_visibility="collapsed")
                lhrtruk4sumbu_trailer = st.number_input ("              ",0, label_visibility="collapsed")
                lhrtruk5sumbu_trailer1 = st.number_input ("               ",0, label_visibility="collapsed")
                lhrtruk5sumbu_trailer2 = st.number_input ("                ",0, label_visibility="collapsed")
                lhrtruk6sumbu_trailer = st.number_input ("                 ",0, label_visibility="collapsed")
            total_lhr = (lhrsepeda_motor + lhrmobil_penumpang + lhrbus_kecil + lhrbus_besar +
                            lhrtruk2sumbu_cargoringan + lhrtruk2sumbu_ringan + lhrtruk2sumbu_cargosedang +
                            lhrtruk2sumbu_sedang + lhrtruk2sumbu_berat1 + lhrtruk2sumbu_berat2 + 
                            lhrtruk3sumbu_ringan + lhrtruk3sumbu_sedang + lhrtruk3sumbu_berat + 
                            lhrtruk2sumbu_dan_trailerpenarik2sumbu + lhrtruk4sumbu_trailer + lhrtruk5sumbu_trailer1 +
                            lhrtruk5sumbu_trailer2 + lhrtruk6sumbu_trailer)

            ## BEBAN LALU LINTAS PADA LAJUR RENCANA DENGAN UMUR RENCANA 40 TAHUN (JUTA ESA5)
            esa_stabilisasi_sepeda_motor = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrsepeda_motor * t2_vdf5sepeda_motor * 0.5)
            esa_stabilisasi_sepeda_motor = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrmobil_penumpang * t2_vdf5mobil_penumpang * 0.5)
            esa_stabilisasi_bus_kecil = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrbus_kecil * t2_vdf5bus_kecil * 0.5)
            esa_stabilisasi_bus_besar = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrbus_besar * t2_vdf5bus_besar * 0.5)
            esa_stabilisasi_truk2sumbu_cargoringan = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_cargoringan * t2_vdf5truk2sumbu_cargoringan * 0.5)
            esa_stabilisasi_truk2sumbu_ringan = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_ringan * t2_vdf5truk2sumbu_ringan * 0.5)
            esa_stabilisasi_truk2sumbu_cargosedang = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_cargosedang * t2_vdf5truk2sumbu_cargosedang * 0.5)
            esa_stabilisasi_truk2sumbu_sedang = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_sedang * t2_vdf5truk2sumbu_sedang * 0.5)
            esa_stabilisasi_truk2sumbu_berat1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_berat1 * t2_vdf5truk2sumbu_berat1 * 0.5)
            esa_stabilisasi_truk2sumbu_berat2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_berat2 * t2_vdf5truk2sumbu_berat2 * 0.5)
            esa_stabilisasi_truk3sumbu_ringan = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk3sumbu_ringan * t2_vdf5truk3sumbu_ringan * 0.5)
            esa_stabilisasi_truk3sumbu_sedang = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk3sumbu_sedang * t2_vdf5truk3sumbu_sedang * 0.5)
            esa_stabilisasi_truk3sumbu_berat = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk3sumbu_berat * t2_vdf5truk3sumbu_berat * 0.5)
            esa_stabilisasi_truk2sumbu_dan_trailerpenarik2sumbu = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk2sumbu_dan_trailerpenarik2sumbu * t2_vdf5truk2sumbu_dan_trailerpenarik2sumbu * 0.5)
            esa_stabilisasi_truk4sumbu_trailer = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk4sumbu_trailer * t2_vdf5truk4sumbu_trailer * 0.5)
            esa_stabilisasi_truk5sumbu_trailer1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk5sumbu_trailer1 * t2_vdf5truk5sumbu_trailer1 * 0.5)
            esa_stabilisasi_truk5sumbu_trailer2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk5sumbu_trailer2 * t2_vdf5truk5sumbu_trailer2 * 0.5)
            esa_stabilisasi_truk6sumbu_trailer = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhrtruk6sumbu_trailer * t2_vdf5truk6sumbu_trailer * 0.5)

            cesa_stabilisasi = math.ceil(esa_stabilisasi_bus_kecil
                                + esa_stabilisasi_bus_besar + esa_stabilisasi_truk2sumbu_cargoringan + esa_stabilisasi_truk2sumbu_ringan
                                + esa_stabilisasi_truk2sumbu_cargosedang + esa_stabilisasi_truk2sumbu_sedang + esa_stabilisasi_truk2sumbu_berat1
                                + esa_stabilisasi_truk2sumbu_berat2 + esa_stabilisasi_truk3sumbu_ringan + esa_stabilisasi_truk3sumbu_sedang
                                + esa_stabilisasi_truk3sumbu_berat + esa_stabilisasi_truk2sumbu_dan_trailerpenarik2sumbu
                                + esa_stabilisasi_truk4sumbu_trailer + esa_stabilisasi_truk5sumbu_trailer1 + esa_stabilisasi_truk6sumbu_trailer)
            tampil_input_cbrt2 = st.checkbox("Input Data CBR")

            with tabs3:
                if tampil_input_cbrt2 :
                    st.write("Format file excel harus sesuai dengan template yang telah disediakan berikut")
                    with open("template.xlsx", "rb") as file:
                        btn = st.download_button(
                                label="Download File Excel",
                                data=file,
                                file_name="template.xlsx",
                                mime="xlsx")

                    ## ------ UPLOAD FILE EXCEL
                    upload_file_excel = st.file_uploader('Masukkan Data CBR Dalam Format xlsx', type='xlsx')
                    if upload_file_excel :
                        st.markdown('---')
                        df = pd.read_excel(upload_file_excel, engine='openpyxl')
                        st.write("Data awal :")
                        st.dataframe(df)
                        staberapa = df['STA']
                        nilaicbr = df['NILAI CBR']
                        koefvar=fkoefvar(df)
                        rata2=df["NILAI CBR"].mean()
                        nstd=df["NILAI CBR"].std()
                        jumlahdata=len(df)
                        df_data_awal = pd.DataFrame(
                                        {
                                            "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi"],
                                            "Hasil" : [(jumlahdata), (rata2), (nstd), (koefvar)]
                                        }
                                    )
                        st.dataframe(df_data_awal)
                        if (koefvar < 30) or (jumlahdata <=10):
                            st.success("Dapat dijadikan satu segemen")
                        else :
                            st.warning("Tidak dapat dijadikan satu segemen")
                        
                        rumus_cbr_karakteristik = st.selectbox("Rumus CBR Karakteristik",['Metode distribusi normal standar',
                                                                                        'Metode persentil',])
                        if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                            pilih_tipe_jalan = st.radio("Tipe Jalan",['Bebas Hambatan', 'Jalan Kolektor atau Arteri', 'Jalan Lokal dan Jalan Kecil'])
                            if pilih_tipe_jalan == 'Jalan Kolektor atau Arteri':
                                f_nilai = 1.282
                            elif pilih_tipe_jalan == 'Bebas Hambatan':
                                f_nilai = 1.645
                            elif pilih_tipe_jalan == 'Jalan Lokal dan Jalan Kecil':
                                f_nilai = 0.842

                        jumlah_segmen = int(st.number_input("Input jumlah segmen :",1))
                        # List untuk menyimpan jumlah data per list yang diinput oleh pengguna
                        data_per_list = []
                        # Memasukkan jumlah data per list sesuai jumlah list yang diinginkan
                        ukuran_bagian=(jumlahdata//jumlah_segmen)
                        junlahdataterambil=ukuran_bagian*jumlah_segmen
                        bagian = []
                        startdata = 0
                        for i in range(jumlah_segmen-1):
                            enddata = min(startdata + ukuran_bagian, jumlahdata)
                            bagian.append(df.iloc[startdata:enddata])
                            startdata=enddata
                        bagian.append(df.iloc[startdata:jumlahdata])
                        statussegmen=False
                        for i in range(jumlah_segmen):
                            jml_data_persegmen = len(bagian[i])
                            data = st.number_input(f"Masukkan banyak data CBR untuk segmen {i+1}", min_value=1, value=jml_data_persegmen)
                            data_per_list.append(data)

                        # Memunculkan hasil pembagian data pada list
                        if st.button("Tampilkan"):
                            if len(df) > 0:
                                lists = divide_into_lists(df, data_per_list)
                                for i, lst in enumerate(lists, start=1):
                                    jumlah_banyak_data_cbr = len(lst)
                                    st.write(f"Segmen ke-{i} dengan jumlah data {jumlah_banyak_data_cbr} dapat dilihat pada tabel berikut :")
                                    st.dataframe(lst)
                                    Nilai_cbr_rata2 = cbr_rata2(lst)
                                    nilai_devstandar = nilai_std(lst)
                                    koefvar=fkoefvar(lst)
                                    if len(lst)>10 and koefvar>30:
                                        statussegmen=True
                                    else :
                                        statussegmen=False
                                    if jumlah_banyak_data_cbr <= 10:
                                        nilai_terkecil_cbr = min((lst["NILAI CBR"]))
                                        cbr_karakteristik = nilai_terkecil_cbr
                                    else :
                                        if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                                            cbr_karakteristik = Nilai_cbr_rata2 - f_nilai * nilai_devstandar
                                        else :
                                            xdata=(lst["NILAI CBR"])
                                            cbr_karakteristik = np.percentile(xdata, 10)
                                    ## -STABILISASI TANAH
                                    if  cbr_karakteristik < 1:
                                        nilai_stabilisasi = "Perlu penangan lebih lanjut"
                                    elif  1 <= cbr_karakteristik < 2.5:
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = 1000
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = 1100
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = 1200
                                    elif  2.5 <= cbr_karakteristik < 3:
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = 175
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = 250
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = 350
                                    elif 3 <= cbr_karakteristik < 4 :
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = 150
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = 200
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = 300
                                    elif 4 <= cbr_karakteristik < 5 :
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = 100
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = 150
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = 200
                                    elif 5 <= cbr_karakteristik < 6 :
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = 100
                                    elif cbr_karakteristik >= 6 :
                                        if cesa_stabilisasi < 2000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif 2000000 <= cesa_stabilisasi <= 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        elif cesa_stabilisasi > 4000000 :
                                            nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                    ## --TABEL HASIL
                                    df_hasil_stabilisasi = pd.DataFrame(
                                        {
                                            "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi", "CBR Karakteristik",
                                                      "Beban lalu lintas pada lajur rencana dengan umur rencana 40 tahun (juta ESA5)" ,
                                                      "Tebal Minimum Material Timbunan Pilihan (mm)", "Stabilisasi Diatas Material Timbunan Pilihan (mm)"],
                                            "Hasil" : [(jumlah_banyak_data_cbr), round(Nilai_cbr_rata2, 3), round(nilai_devstandar, 3), round(koefvar, 3), 
                                                    round(cbr_karakteristik, 3), (cesa_stabilisasi), (nilai_stabilisasi), ("150")]
                                        }
                                    )
                                    st.dataframe(df_hasil_stabilisasi)
                                    # st.warning(koefvar)
                                    if statussegmen:
                                        st.warning("Sebaiknya dibagi segmen lagi")
                                    else:
                                        st.success(f"Segmen {i} memenuhi")

                                    
                    ######################### TABS 3 #################################
                    with tabs4:
                        if tampil_input_lhr :
                            HASIL_t2 = st.checkbox ("Hasil")
                            if HASIL_t2 :
                                ## Beban Lalu Lintas Desain 1 persen
                                E1p_sepeda_motor = math.ceil(365 * 22 * lhrsepeda_motor * t2_vdf4sepeda_motor * DD * DL)
                                E1p_mobil_penumpang = math.ceil(365 * 22 * lhrmobil_penumpang * t2_vdf4mobil_penumpang * DD * DL)
                                E1p_bus_kecil = math.ceil(365 * 22 * lhrbus_kecil * t2_vdf4bus_kecil * DD * DL)
                                E1p_bus_besar = math.ceil(365 * 22 * lhrbus_besar * t2_vdf4bus_besar * DD * DL)
                                E1p_truk2sumbu_cargoringan = math.ceil(365 * 22 * lhrtruk2sumbu_cargoringan * t2_vdf4truk2sumbu_cargoringan * DD * DL)
                                E1p_truk2sumbu_ringan = math.ceil(365 * 22 * lhrtruk2sumbu_ringan * t2_vdf4truk2sumbu_ringan * DD * DL)
                                E1p_truk2sumbu_cargosedang = math.ceil(365 * 22 * lhrtruk2sumbu_cargosedang * t2_vdf4truk2sumbu_cargosedang * DD * DL)
                                E1p_truk2sumbu_sedang = math.ceil(365 * 22 * lhrtruk2sumbu_sedang * t2_vdf4truk2sumbu_sedang * DD * DL)
                                E1p_truk2sumbu_berat1 = math.ceil(365 * 22 * lhrtruk2sumbu_berat1 * t2_vdf4truk2sumbu_berat1 * DD * DL)
                                E1p_truk2sumbu_berat2 = math.ceil(365 * 22 * lhrtruk2sumbu_berat2 * t2_vdf4truk2sumbu_berat2 * DD * DL)
                                E1p_truk3sumbu_ringan = math.ceil(365 * 22 * lhrtruk3sumbu_ringan * t2_vdf4truk3sumbu_ringan * DD * DL)
                                E1p_truk3sumbu_sedang = math.ceil(365 * 22 * lhrtruk3sumbu_sedang * t2_vdf4truk3sumbu_sedang * DD * DL)
                                E1p_truk3sumbu_berat = math.ceil(365 * 22 * lhrtruk3sumbu_berat * t2_vdf4truk3sumbu_berat * DD * DL)
                                E1p_truk2sumbu_dan_trailerpenarik2sumbu = math.ceil(365 * 22 * lhrtruk2sumbu_dan_trailerpenarik2sumbu * t2_vdf4truk2sumbu_dan_trailerpenarik2sumbu * DD * DL)
                                E1p_truk4sumbu_trailer = math.ceil(365 * 22 * lhrtruk4sumbu_trailer * t2_vdf4truk4sumbu_trailer * DD * DL)
                                E1p_truk5sumbu_trailer1 = math.ceil(365 * 22 * lhrtruk5sumbu_trailer1 * t2_vdf4truk5sumbu_trailer1 * DD * DL)
                                E1p_truk5sumbu_trailer2 = math.ceil(365 * 22 * lhrtruk5sumbu_trailer2 * t2_vdf4truk5sumbu_trailer2 * DD * DL)
                                E1p_truk6sumbu_trailer = math.ceil(365 * 22 * lhrtruk6sumbu_trailer * t2_vdf4truk6sumbu_trailer * DD * DL)

                                bebanlalulintasdesain1p = (E1p_bus_kecil + E1p_bus_besar + E1p_truk2sumbu_cargoringan
                                                        + E1p_truk2sumbu_ringan + E1p_truk2sumbu_cargosedang + E1p_truk2sumbu_sedang + E1p_truk2sumbu_berat1
                                                        + E1p_truk2sumbu_berat2 + E1p_truk3sumbu_ringan + E1p_truk3sumbu_sedang + E1p_truk3sumbu_berat
                                                        + E1p_truk2sumbu_dan_trailerpenarik2sumbu + E1p_truk4sumbu_trailer + E1p_truk5sumbu_trailer1
                                                        + E1p_truk5sumbu_trailer2 + E1p_truk6sumbu_trailer)
                                            
                                ## Beban Lalu Lintas Desain 28,2 persen
                                E3p_sepeda_motor = math.ceil(365 * 28.2 * lhrsepeda_motor * t2_vdf4sepeda_motor * DD * DL)
                                E3p_mobil_penumpang = math.ceil(365 * 28.2 * lhrmobil_penumpang * t2_vdf4mobil_penumpang * DD * DL)
                                E3p_bus_kecil = math.ceil(365 * 28.2 * lhrbus_kecil * t2_vdf4bus_kecil * DD * DL)
                                E3p_bus_besar = math.ceil(365 * 28.2 * lhrbus_besar * t2_vdf4bus_besar * DD * DL)
                                E3p_truk2sumbu_cargoringan = math.ceil(365 * 28.2 * lhrtruk2sumbu_cargoringan * t2_vdf4truk2sumbu_cargoringan * DD * DL)
                                E3p_truk2sumbu_ringan = math.ceil(365 * 28.2 * lhrtruk2sumbu_ringan * t2_vdf4truk2sumbu_ringan * DD * DL)
                                E3p_truk2sumbu_cargosedang = math.ceil(365 * 28.2 * lhrtruk2sumbu_cargosedang * t2_vdf4truk2sumbu_cargosedang * DD * DL)
                                E3p_truk2sumbu_sedang = math.ceil(365 * 28.2 * lhrtruk2sumbu_sedang * t2_vdf4truk2sumbu_sedang * DD * DL)
                                E3p_truk2sumbu_berat1 = math.ceil(365 * 28.2 * lhrtruk2sumbu_berat1 * t2_vdf4truk2sumbu_berat1 * DD * DL)
                                E3p_truk2sumbu_berat2 = math.ceil(365 * 28.2 * lhrtruk2sumbu_berat2 * t2_vdf4truk2sumbu_berat2 * DD * DL)
                                E3p_truk3sumbu_ringan = math.ceil(365 * 28.2 * lhrtruk3sumbu_ringan * t2_vdf4truk3sumbu_ringan * DD * DL)
                                E3p_truk3sumbu_sedang = math.ceil(365 * 28.2 * lhrtruk3sumbu_sedang * t2_vdf4truk3sumbu_sedang * DD * DL)
                                E3p_truk3sumbu_berat = math.ceil(365 * 28.2 * lhrtruk3sumbu_berat * t2_vdf4truk3sumbu_berat * DD * DL)
                                E3p_truk2sumbu_dan_trailerpenarik2sumbu = math.ceil(365 * 28.2 * lhrtruk2sumbu_dan_trailerpenarik2sumbu * t2_vdf4truk2sumbu_dan_trailerpenarik2sumbu * DD * DL)
                                E3p_truk4sumbu_trailer = math.ceil(365 * 28.2 * lhrtruk4sumbu_trailer * t2_vdf4truk4sumbu_trailer * DD * DL)
                                E3p_truk5sumbu_trailer1 = math.ceil(365 * 28.2 * lhrtruk5sumbu_trailer1 * t2_vdf4truk5sumbu_trailer1 * DD * DL)
                                E3p_truk5sumbu_trailer2 = math.ceil(365 * 28.2 * lhrtruk5sumbu_trailer2 * t2_vdf4truk5sumbu_trailer2 * DD * DL)
                                E3p_truk6sumbu_trailer = math.ceil(365 * 28.2 * lhrtruk6sumbu_trailer * t2_vdf4truk6sumbu_trailer * DD * DL)

                                bebanlalulintasdesain3p = (E3p_bus_kecil + E3p_bus_besar + E3p_truk2sumbu_cargoringan
                                                        + E3p_truk2sumbu_ringan + E3p_truk2sumbu_cargosedang + E3p_truk2sumbu_sedang + E3p_truk2sumbu_berat1
                                                        + E3p_truk2sumbu_berat2 + E3p_truk3sumbu_ringan + E3p_truk3sumbu_sedang + E3p_truk3sumbu_berat
                                                        + E3p_truk2sumbu_dan_trailerpenarik2sumbu + E3p_truk4sumbu_trailer + E3p_truk5sumbu_trailer1
                                                        + E3p_truk5sumbu_trailer2 + E3p_truk6sumbu_trailer)
                                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas' :
                                    beban_lalin_desain_t2 = bebanlalulintasdesain1p
                                elif deskripsi_jalan == 'Jalan kecil dua arah' :
                                    beban_lalin_desain_t2 = bebanlalulintasdesain1p
                                elif deskripsi_jalan == 'Jalan lokal' :
                                    beban_lalin_desain_t2 = bebanlalulintasdesain1p
                                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry':
                                    beban_lalin_desain_t2 = bebanlalulintasdesain3p
                                elif deskripsi_jalan == 'Jalan kolektor':
                                    beban_lalin_desain_t2 = bebanlalulintasdesain3p
                                            
                                ## PERSEN KENDARAAN BERAT TABEL 2
                                jmlkendberat = (lhrbus_kecil + lhrbus_besar + lhrtruk2sumbu_cargoringan + lhrtruk2sumbu_ringan + lhrtruk2sumbu_cargosedang
                                                + lhrtruk2sumbu_sedang + lhrtruk2sumbu_berat1 + lhrtruk2sumbu_berat2 + lhrtruk3sumbu_ringan
                                                + lhrtruk3sumbu_sedang + lhrtruk3sumbu_berat + lhrtruk2sumbu_dan_trailerpenarik2sumbu
                                                + lhrtruk4sumbu_trailer + lhrtruk5sumbu_trailer1 + lhrtruk5sumbu_trailer2 + lhrtruk6sumbu_trailer)
                                                
                                jmlsemuakend = (lhrbus_kecil + lhrbus_besar + lhrtruk2sumbu_cargoringan + lhrtruk2sumbu_ringan + lhrtruk2sumbu_cargosedang
                                                + lhrtruk2sumbu_sedang + lhrtruk2sumbu_berat1 + lhrtruk2sumbu_berat2 + lhrtruk3sumbu_ringan
                                                + lhrtruk3sumbu_sedang + lhrtruk3sumbu_berat + lhrtruk2sumbu_dan_trailerpenarik2sumbu
                                                + lhrtruk4sumbu_trailer + lhrtruk5sumbu_trailer1 + lhrtruk5sumbu_trailer2 + lhrtruk6sumbu_trailer
                                                + lhrsepeda_motor + lhrmobil_penumpang)

                                persenkendberat = ((jmlkendberat / jmlsemuakend)*100)

                                # TABEL LALU LINTAS BERAT TABEL 2
                                ### Perhitungan ESAL Tiap Kendaraan
                                esalsepeda_motor = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrsepeda_motor * 0)
                                esalmobil_penumpang = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrmobil_penumpang * 0)
                                esalbus_kecil = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrbus_kecil * 2)
                                esalbus_besar = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrbus_besar * 2)
                                esaltruk2sumbu_cargoringan = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_cargoringan * 2)
                                esaltruk2sumbu_ringan = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_ringan * 2)
                                esaltruk2sumbu_cargosedang = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_cargosedang * 2)
                                esaltruk2sumbu_sedang = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_sedang * 2)
                                esaltruk2sumbu_berat1 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_berat1 * 2)
                                esaltruk2sumbu_berat2 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_berat2 * 2)
                                esaltruk3sumbu_ringan = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk3sumbu_ringan * 2)
                                esaltruk3sumbu_sedang = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk3sumbu_sedang * 2)
                                esaltruk3sumbu_berat = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk3sumbu_berat * 2)
                                esaltruk2sumbu_dan_trailerpenarik2sumbu = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk2sumbu_dan_trailerpenarik2sumbu * 4)
                                esaltruk4sumbu_trailer = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk4sumbu_trailer * 3)
                                esaltruk5sumbu_trailer1 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk5sumbu_trailer1 * 3)
                                esaltruk5sumbu_trailer2 = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk5sumbu_trailer2 * 3)
                                esaltruk6sumbu_trailer = math.ceil(365 * faktor_pengali_pertumbuhan_lalu_lintas * DL * DD * lhrtruk6sumbu_trailer * 3)
                                                        
                                # Menghitung CESAL
                                comulative_esal = math.ceil(esalbus_kecil + esalbus_besar + esaltruk2sumbu_cargoringan + esaltruk2sumbu_ringan
                                                            + esaltruk2sumbu_cargosedang + esaltruk2sumbu_sedang + esaltruk2sumbu_berat1 + esaltruk2sumbu_berat2
                                                            + esaltruk3sumbu_ringan + esaltruk3sumbu_sedang + esaltruk3sumbu_berat + esaltruk2sumbu_dan_trailerpenarik2sumbu
                                                            + esaltruk4sumbu_trailer + esaltruk5sumbu_trailer1 + esaltruk5sumbu_trailer2 + esaltruk6sumbu_trailer
                                                            + esalsepeda_motor)
                                # Perencanaan Tebal Perkerasan Lalu
                                if comulative_esal < 4300000 :
                                    LB_Tebal_Perkerasan_Beton = 265
                                elif 4300000 <= comulative_esal < 8600000 :
                                    LB_Tebal_Perkerasan_Beton = 275
                                elif 8600000 <= comulative_esal < 25800000 :
                                    LB_Tebal_Perkerasan_Beton = 285
                                elif 25800000 <= comulative_esal < 43000000 :
                                    LB_Tebal_Perkerasan_Beton = 295
                                elif comulative_esal >= 43000000 :
                                    LB_Tebal_Perkerasan_Beton = 305
                                def diamater_dowel_t2() :
                                    if 265 <= LB_Tebal_Perkerasan_Beton <= 275 :
                                        d_dowel = 32
                                        return d_dowel
                                    elif 285 <= LB_Tebal_Perkerasan_Beton <= 305 :
                                        d_dowel = 40
                                        return d_dowel
                                def diamater_tiebar_t2() :
                                    luas_penampang_tulangan = 204 * (LB_Tebal_Perkerasan_Beton / 1000) * lebar_lajur
                                    if luas_penampang_tulangan <= 201 :
                                        diamater_tiebar = 16
                                        return diamater_tiebar
                                    elif 201 < luas_penampang_tulangan <= 284 :
                                        diamater_tiebar = 19
                                        return diamater_tiebar
                                    elif 284 < luas_penampang_tulangan <= 380 :
                                        diamater_tiebar = 22
                                        return diamater_tiebar
                                    elif 380 < luas_penampang_tulangan <= 491 :
                                        diamater_tiebar = 25
                                        return diamater_tiebar
                                    elif 491 < luas_penampang_tulangan <= 661 :
                                        diamater_tiebar = 29
                                        return diamater_tiebar
                                    elif 661 < luas_penampang_tulangan <= 804 :
                                        diamater_tiebar = 32
                                        return diamater_tiebar
                                    elif 804 < luas_penampang_tulangan <= 1018 :
                                        diamater_tiebar = 36
                                        return diamater_tiebar
                                    elif 1018 < luas_penampang_tulangan <= 1257 :
                                        diamater_tiebar = 40
                                        return diamater_tiebar
                                    elif 1257 < luas_penampang_tulangan <= 1964 :
                                        diamater_tiebar = 50
                                        return diamater_tiebar
                                    elif 1964 < luas_penampang_tulangan <= 2290 :
                                        diamater_tiebar = 54
                                        return diamater_tiebar
                                    elif 2290 < luas_penampang_tulangan <= 2552 :
                                        diamater_tiebar = 57
                                        return diamater_tiebar
                                def panjang_batang_pengikat_t2() :
                                    panjang_batang_pengikat = (38.3 * diamater_tiebar_t2()) + 75
                                    return panjang_batang_pengikat
                                def lalin_berat_t2() :    
                                    df_tebal_perkerasan = pd.DataFrame(
                                        {
                                            "Parameter" : [
                                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)", "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                                "Lalu Lintas (Berat/Rendah)", "Komulatif Kelompok Sumbu Kendaraan Berat", "Menggunakan Bahu Pelat Beton",
                                                "Tebal Perkerasan Beton (mm)", "Diameter Dowel (mm)" , "Panjang Dowel (mm)", "Jarak Antar Dowel (mm)",
                                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "Lapis Fondasi LMC (mm)",
                                                "Lapis Dainase (mm)"
                                            ],
                                            "Hasil" : [
                                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr), (beban_lalin_desain_t2), ("Berat"),
                                                (comulative_esal), 
                                                ("Ya"), (LB_Tebal_Perkerasan_Beton), (diamater_dowel_t2()), ("450"), ("300"),
                                                (diamater_tiebar_t2()), round(panjang_batang_pengikat_t2(), 3), ("750"),("100"), ("150")
                                            ]
                                        }
                                    )
                                    return st.dataframe(df_tebal_perkerasan) 

                                def lalin_rendah_t2() :
                                    keadaan_tanah_dasar = st.selectbox("Tanah Dasar",['Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton',
                                                                                'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton',
                                                                                'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton',
                                                                                'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton'])
                                    if keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton' :
                                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                                        bahu_jalan = "Ya"
                                        tulangan_distribusi_retak = "Ya"
                                        if jmlkendberat == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah= 180
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton' :
                                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                                        bahu_jalan = "Tidak"
                                        tulangan_distribusi_retak = "Ya"
                                        if jmlkendberat == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 200
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton' :
                                        tanah_dasar = "Dipadatkan Normal"
                                        bahu_jalan = "Ya"
                                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                                        if jmlkendberat == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 135
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                                            dapat_dilalui_truk = "Ya"
                                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton' :
                                        tanah_dasar = "Dipadatkan Normal"
                                        bahu_jalan = "Tidak"
                                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                                        if jmlkendberat == 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 150
                                            dapat_dilalui_truk = "Tidak"
                                        elif jmlkendberat > 0 :
                                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                                            dapat_dilalui_truk = "Ya"
                                    df_tebal_perkerasan = pd.DataFrame(
                                        {
                                            "Parameter" : [
                                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)",
                                                "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                                "Lalu Lintas (Berat/Rendah)", "Tanah Dasar", "Menggunakan Bahu Pelat Beton", "Dapat Dilalui Truk",
                                                "Tebal Perkerasan Beton (mm)", "Tulangan Distribusi Retak", "Dowel" ,
                                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "LMC (mm)",
                                                "Lapis Fondasi Kelas A (Ukuran Butir Nominal Maksimum 30 mm) (mm)", "Jarak Sambungan Melintang (m)"
                                            ],
                                            "Hasil" : [
                                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr), (beban_lalin_desain_t2), ("Rendah"), 
                                                (tanah_dasar), (bahu_jalan), (dapat_dilalui_truk),
                                                (LR_Tebal_Perkerasan_Beton_Rendah), (tulangan_distribusi_retak), ("Tidak Dibutuhkan"), 
                                                (diamater_tiebar_t2()), round(panjang_batang_pengikat_t2(), 3), ("750"), ("Tidak Dibutuhkan"),
                                                ("125"), ("4")
                                            ]
                                        }
                                    )
                                    return st.dataframe(df_tebal_perkerasan)                    
                                 
                                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas' :
                                    if bebanlalulintasdesain1p > 45000 :
                                        lalin_berat_t2()
                                    else :
                                        lalin_rendah_t2()
                                elif deskripsi_jalan == 'Jalan kecil dua arah' :
                                    if bebanlalulintasdesain1p > 70000 :
                                        lalin_berat_t2()
                                    else :
                                        lalin_rendah_t2()
                                elif deskripsi_jalan == 'Jalan lokal' :
                                    if bebanlalulintasdesain1p > 800000 :
                                        lalin_berat_t2()
                                    else :
                                        lalin_rendah_t2()
                                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry' :
                                    if bebanlalulintasdesain3p > 1500000 :
                                        lalin_berat_t2()
                                    else :
                                        lalin_rendah_t2()
                                elif deskripsi_jalan == 'Jalan kolektor' :
                                    if bebanlalulintasdesain3p > 5000000 :
                                        lalin_berat_t2()
                                    else :
                                        lalin_rendah_t2() 

### ------------- TABEL 3 --------------- ###
if (selected == 'Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga Suplemen MDPJ 2017') :
    st.title('Desain Perkerasan Kaku NIlai VDF Kendaraan Niaga Suplemen MDPJ 2017')
    # membuat tabs
    tabs1, tabs2, tabs3 , tabs4 = st.tabs(["Input Deskripsi Umum", "Input Data Lalu Lintas Harian", "Menghitung Stabilisasi Tanah", "Menghitung Perkerasan Kaku"])
    ########################## TABS 1 ############################
    with tabs1:
        ## Membagi Kolom
        col1, col2 = st.columns(2)
        # Deskripsi Jalan
        jalan = ['Jalan desa minor dengan akses kendaraan berat terbatas','Jalan kecil dua arah'
                 ,'Jalan lokal','Akses lokal daerah industri atau quarry','Jalan kolektor']
        deskripsi_jalan = st.radio("Deskripsi Jalan", jalan)
        # Daerah
        Daerah_Tabel3 = ['Aceh dan Sumatera Utara', 'Bali', 'Bangka Belitung', 'Banten - Lintas Tengah',
                         'Banten - Pantura', 'Bengkulu', 'Daerah Istimewa Yogyakarta', 'DKI Pantura (Cakung-Ciliking)',
                         'Gorontalo - Sulteng - Sultra', 'Jambi', 'Jawa Barat - Pantura', 'Jawa Barat (Lintas Tengah)',
                         'Jawa Tengah - Pantura', 'Jawa Timur - Pantura', 'Jawa Timur Jalan Lintas Selatan',
                         'Jawa Timur Jalan Lintas Tengah', 'Jawa Timur Jalan Penghubung Lintas Pulau Jawa',
                         'Kalimantan Barat / Kalimantan Tengah', 'Kalimantan Selatan', 'Kalimantan Timut', 'Kalimantan Utara','Kepulauan Riau',
                         'Lampung (Jalan Lintas Timur)', 'Nusa Tenggara Timur - Maluku - Maluku Utara - Papua Barat - Papua',
                         'Nusa Tenggara Barat', 'Riau', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Utara',
                         'Sumatera Barat Lintas Barat Pesisir Selatan', 'Sumatera Barat Lintas Barat Pesisir Utara',
                         'Sumatera Barat Lintas Tengah Selatan', 'Sumatera Barat Lintas Tengah Utara', 'Sumatera Selatan (Jalan Lintas Timur)',]
        Daerah_tinjauan = st.selectbox("Daerah Yang Ditinjau", Daerah_Tabel3)
        with col1:
            # Faktor Distibusi Lajur
            DL = (st.number_input("Masukkan Nilai Faktor Distribusi Lajur (DL)", value =  0.5))
            # Faktor Distribusi Arah
            DD = st.number_input("Masukkan Nilai Faktor Distribusi Arah (DD)", value = 0.5)
            # Lebar Lajur
            lebar_lajur = (st.number_input ("Lebar Lajur (m)", value = 3.0))
        with col2:
            # Umur Rencana
            UR = (st.number_input ("Masukka Umur Rencana (UR)", min_value=0, value = 40))
            # Faktor Laju Pertumbuhan Lalu Lintas (i)
            i = (st.number_input ("Masukkan Nilai Faktor Laju Pertumbuhan Lalu Lintas (i)", value = 1.0))
        # Faktor Pengali Pertumbuhan Lalu Lintas (R)
        faktor_pengali_pertumbuhan_lalu_lintas = ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i))
        tampil_input_lhr = st.checkbox("Lanjutkan")
        with tabs2:
            if tampil_input_lhr :
                ## Membagi Kolom
                col1, col2, col3 = st.columns(3)
                with col1 :
                    st.write("Jenis Kendaraan")
                    st.write("2,3,4")
                    st.write(" ")
                    st.write("5A")
                    st.write(" ")
                    st.write("5B")
                    st.write(" ")
                    st.write("6A")
                    st.write(" ")
                    st.write("6B")
                    st.write(" ") 
                    st.write("7A1")
                    st.write(" ")
                    st.write("7A2")
                    st.write(" ")
                    st.write("7B1")
                    st.write(" ")
                    st.write("7B2")
                    st.write(" ")
                    st.write("7C1")
                    st.write(" ")
                    st.write("7C2A")
                    st.write(" ")
                    st.write("7C2B")
                    st.write("7C3")
                with col2 :
                    st.write("Lalu Lintas Harian Rata-Rata")
                    lhr234_t3 = st.number_input ("                  ", min_value=0,value = 10, label_visibility="collapsed")
                    lhr5A_t3 = st.number_input ("",min_value=0,value = 10, label_visibility="collapsed")
                    lhr5B_t3 = st.number_input (" ",0, label_visibility="collapsed")
                    lhr6A_t3 = st.number_input ("  ",0, label_visibility="collapsed")
                    lhr6B_t3 = st.number_input ("   ",0, label_visibility="collapsed")
                    lhr7A1_t3 = st.number_input ("    ",0, label_visibility="collapsed")
                    lhr7A2_t3 = st.number_input ("     ",0, label_visibility="collapsed")
                    lhr7B1_t3 = st.number_input ("      ",0, label_visibility="collapsed")
                    lhr7B2_t3 = st.number_input ("        ",0, label_visibility="collapsed")
                    lhr7C1_t3 = st.number_input ("         ",0, label_visibility="collapsed")
                    lhr7C2A_t3 = st.number_input ("          ",0, label_visibility="collapsed")
                    lhr7C2B_t3 = st.number_input ("           ",0, label_visibility="collapsed")
                    lhr7C3_t3 = st.number_input ("            ",0, label_visibility="collapsed")

                jmlkendberat_t3 = (lhr234_t3 + lhr5A_t3 + lhr5B_t3 + lhr6A_t3 + lhr6B_t3 + lhr7A1_t3 + lhr7A2_t3
                                + lhr7B1_t3 + lhr7B2_t3 + lhr7C1_t3 + lhr7C2A_t3 + lhr7C2B_t3 + lhr7C3_t3) 
                                            
                if Daerah_tinjauan == 'Aceh dan Sumatera Utara' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.9
                    t3_BA_VDF5_7A1 = 10.8
                    t3_BA_VDF5_7A2 = 19.5
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 16.6
                    t3_BA_VDF5_7C2A = 9.8
                    t3_BA_VDF5_7C2B = 32.5
                    t3_BA_VDF5_7C3 = 29.5
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2
                    t3_BA_VDF4_7A1 = 11
                    t3_BA_VDF4_7A2 = 10.2
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 10.3
                    t3_BA_VDF4_7C2A = 6.7
                    t3_BA_VDF4_7C2B = 15.1
                    t3_BA_VDF4_7C3 = 16
                elif Daerah_tinjauan == 'Bali' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 7.3
                    t3_BA_VDF5_7A1 = 12.3
                    t3_BA_VDF5_7A2 = 23.6
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 15.3
                    t3_BA_VDF5_7C2A = 9.6
                    t3_BA_VDF5_7C2B = 20.7
                    t3_BA_VDF5_7C3 = 11.9
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 4.8
                    t3_BA_VDF4_7A1 = 7.8
                    t3_BA_VDF4_7A2 = 12.4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 9.8
                    t3_BA_VDF4_7C2A = 6.2
                    t3_BA_VDF4_7C2B = 11.3
                    t3_BA_VDF4_7C3 = 7.2
                elif Daerah_tinjauan == 'Bangka Belitung' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.7
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 13
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 0
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 7.4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 0
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Banten - Lintas Tengah' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 7.7
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 10.2
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 9.9
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 5.3
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 6.1
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 6.6
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Banten - Pantura' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 5
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 5.9
                    t3_BA_VDF5_7B1 = 9.5
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 8.2
                    t3_BA_VDF5_7C2A = 12.9
                    t3_BA_VDF5_7C2B = 13.2
                    t3_BA_VDF5_7C3 = 16.3
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3.3
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 3.5
                    t3_BA_VDF4_7B1 = 6.5
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 5.2
                    t3_BA_VDF4_7C2A = 7.4
                    t3_BA_VDF4_7C2B = 7.5
                    t3_BA_VDF4_7C3 = 9.4
                elif Daerah_tinjauan == 'Bengkulu' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.7
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 13
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 0
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 7.4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 0
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Daerah Istimewa Yogyakarta' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 6.2
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 10.4
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 11.2
                    t3_BA_VDF5_7C2A = 5.3
                    t3_BA_VDF5_7C2B = 8.1
                    t3_BA_VDF5_7C3 = 6.7
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 4.4
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 6.3
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 7.2
                    t3_BA_VDF4_7C2A = 3.6
                    t3_BA_VDF4_7C2B = 6.2
                    t3_BA_VDF4_7C3 = 5.2
                elif Daerah_tinjauan == 'DKI Pantura (Cakung-Ciliking)' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 3.8
                    t3_BA_VDF5_7A1 = 5.2
                    t3_BA_VDF5_7A2 = 7.2
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 4.5
                    t3_BA_VDF5_7C2A = 7.6
                    t3_BA_VDF5_7C2B = 7
                    t3_BA_VDF5_7C3 = 6
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.9
                    t3_BA_VDF4_7A1 = 3.7
                    t3_BA_VDF4_7A2 = 4.9
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 3.6
                    t3_BA_VDF4_7C2A = 5.4
                    t3_BA_VDF4_7C2B = 4.9
                    t3_BA_VDF4_7C3 = 4.3
                elif Daerah_tinjauan == 'Gorontalo - Sulteng - Sultra' : 
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 1.2
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 35.6
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 32.8
                    t3_BA_VDF5_7C2A = 47.8
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 49
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 17.4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 18.1
                    t3_BA_VDF4_7C2A = 24.5
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 24.9
                elif Daerah_tinjauan == 'Jambi' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.4
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 26.9
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 50.7
                    t3_BA_VDF5_7C2A = 39
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 18.1
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 14.3
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 22.9
                    t3_BA_VDF4_7C2A = 18.6
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 10.1
                elif Daerah_tinjauan == 'Jawa Barat - Pantura' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 7.2
                    t3_BA_VDF5_7A1 = 12.6
                    t3_BA_VDF5_7A2 = 33.6
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 18.3
                    t3_BA_VDF5_7C1 = 12.9
                    t3_BA_VDF5_7C2A = 74.2
                    t3_BA_VDF5_7C2B = 40
                    t3_BA_VDF5_7C3 = 40.9
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 4.8
                    t3_BA_VDF4_7A1 = 8
                    t3_BA_VDF4_7A2 = 16.2
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 12.5
                    t3_BA_VDF4_7C1 = 8.4
                    t3_BA_VDF4_7C2A = 31.5
                    t3_BA_VDF4_7C2B = 19.3
                    t3_BA_VDF4_7C3 = 20.9
                elif Daerah_tinjauan == 'Jawa Barat (Lintas Tengah)' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 6.9
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 9.5
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 6.9
                    t3_BA_VDF5_7C2A = 3.5
                    t3_BA_VDF5_7C2B = 5.4
                    t3_BA_VDF5_7C3 = 5.6
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 4.6
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 5.8
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 4.6
                    t3_BA_VDF4_7C2A = 2.6
                    t3_BA_VDF4_7C2B = 4.2
                    t3_BA_VDF4_7C3 = 4.4
                elif Daerah_tinjauan == 'Jawa Tengah - Pantura' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.3
                    t3_BA_VDF5_7A1 = 26.9
                    t3_BA_VDF5_7A2 = 22.2
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 19.6
                    t3_BA_VDF5_7C1 = 19
                    t3_BA_VDF5_7C2A = 36.2
                    t3_BA_VDF5_7C2B = 29.8
                    t3_BA_VDF5_7C3 = 43.8
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3.1
                    t3_BA_VDF4_7A1 = 14.8
                    t3_BA_VDF4_7A2 = 11.2
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 12.2
                    t3_BA_VDF4_7C1 = 11.7
                    t3_BA_VDF4_7C2A = 19.6
                    t3_BA_VDF4_7C2B = 15.7
                    t3_BA_VDF4_7C3 = 22.2
                elif Daerah_tinjauan == 'Jawa Timur - Pantura' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 3.7
                    t3_BA_VDF5_7A1 = 12.4
                    t3_BA_VDF5_7A2 = 28.4
                    t3_BA_VDF5_7B1 = 16.4
                    t3_BA_VDF5_7B2 = 25.9
                    t3_BA_VDF5_7C1 = 20.8
                    t3_BA_VDF5_7C2A = 43.9
                    t3_BA_VDF5_7C2B = 41.8
                    t3_BA_VDF5_7C3 = 44.2
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.6
                    t3_BA_VDF4_7A1 = 8.1
                    t3_BA_VDF4_7A2 = 14.3
                    t3_BA_VDF4_7B1 = 10.1
                    t3_BA_VDF4_7B2 = 17
                    t3_BA_VDF4_7C1 = 12.7
                    t3_BA_VDF4_7C2A = 21.7
                    t3_BA_VDF4_7C2B = 21.2
                    t3_BA_VDF4_7C3 = 22.3
                elif Daerah_tinjauan == 'Jawa Timur Jalan Lintas Selatan' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.7
                    t3_BA_VDF5_7A1 = 7.1
                    t3_BA_VDF5_7A2 = 31.3
                    t3_BA_VDF5_7B1 = 28.9
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 16.5
                    t3_BA_VDF5_7C2A = 37.1
                    t3_BA_VDF5_7C2B = 31.5
                    t3_BA_VDF5_7C3 = 74
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2
                    t3_BA_VDF4_7A1 = 4.7
                    t3_BA_VDF4_7A2 = 15.7
                    t3_BA_VDF4_7B1 = 17.6
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 10.4
                    t3_BA_VDF4_7C2A = 21
                    t3_BA_VDF4_7C2B = 16.5
                    t3_BA_VDF4_7C3 = 35
                elif Daerah_tinjauan == 'Jawa Timur Jalan Lintas Tengah':
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 5.9
                    t3_BA_VDF5_7A1 = 16.8
                    t3_BA_VDF5_7A2 = 37.8
                    t3_BA_VDF5_7B1 = 52.6
                    t3_BA_VDF5_7B2 = 26.5
                    t3_BA_VDF5_7C1 = 25
                    t3_BA_VDF5_7C2A = 50.1
                    t3_BA_VDF5_7C2B = 76.9
                    t3_BA_VDF5_7C3 = 70.3
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3.8
                    t3_BA_VDF4_7A1 = 10.5
                    t3_BA_VDF4_7A2 = 18.8
                    t3_BA_VDF4_7B1 = 29.4
                    t3_BA_VDF4_7B2 = 18
                    t3_BA_VDF4_7C1 = 15.8
                    t3_BA_VDF4_7C2A = 24.5
                    t3_BA_VDF4_7C2B = 30.9
                    t3_BA_VDF4_7C3 = 35.4
                elif Daerah_tinjauan == 'Jawa Timur Jalan Penghubung Lintas Pulau Jawa':
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 1.7
                    t3_BA_VDF5_7A1 = 6.5
                    t3_BA_VDF5_7A2 = 9.4
                    t3_BA_VDF5_7B1 = 3.4
                    t3_BA_VDF5_7B2 = 9.2
                    t3_BA_VDF5_7C1 = 19.8
                    t3_BA_VDF5_7C2A = 11.7
                    t3_BA_VDF5_7C2B = 8.4
                    t3_BA_VDF5_7C3 = 14.8
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.2
                    t3_BA_VDF4_7A1 = 4.7
                    t3_BA_VDF4_7A2 = 5.9
                    t3_BA_VDF4_7B1 = 2.5
                    t3_BA_VDF4_7B2 = 7.2
                    t3_BA_VDF4_7C1 = 12.5
                    t3_BA_VDF4_7C2A = 7.5
                    t3_BA_VDF4_7C2B = 5.4
                    t3_BA_VDF4_7C3 = 9
                elif Daerah_tinjauan == 'Kalimantan Barat / Kalimantan Tengah' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.4
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 8.3
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 5.1
                    t3_BA_VDF5_7C2A = 30.3
                    t3_BA_VDF5_7C2B = 19.9
                    t3_BA_VDF5_7C3 = 13.3
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 4.8
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 3.4
                    t3_BA_VDF4_7C2A = 15.5
                    t3_BA_VDF4_7C2B = 10.4
                    t3_BA_VDF4_7C3 = 7.6
                elif Daerah_tinjauan == 'Kalimantan Selatan':
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 3.1
                    t3_BA_VDF5_7A1 = 6.5
                    t3_BA_VDF5_7A2 = 12.1
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 12.2
                    t3_BA_VDF5_7C2A = 15.9
                    t3_BA_VDF5_7C2B = 9.7
                    t3_BA_VDF5_7C3 = 15.5
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.3
                    t3_BA_VDF4_7A1 = 3.9
                    t3_BA_VDF4_7A2 = 6.7
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 7.7
                    t3_BA_VDF4_7C2A = 9.4
                    t3_BA_VDF4_7C2B = 5.2
                    t3_BA_VDF4_7C3 = 8.9
                elif Daerah_tinjauan == 'Kalimantan Timut' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 5.7
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 11.3
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 5.8
                    t3_BA_VDF5_7C2A = 9.9
                    t3_BA_VDF5_7C2B = 2.6
                    t3_BA_VDF5_7C3 = 1.6
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3.3
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 6.8
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 4.2
                    t3_BA_VDF4_7C2A = 6.9
                    t3_BA_VDF4_7C2B = 1.8
                    t3_BA_VDF4_7C3 = 1.7
                elif Daerah_tinjauan == 'Kalimantan Utara':
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 1.4
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 9.8
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 4.7
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.1
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 6.5
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 3.7
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Kepulauan Riau' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.3
                    t3_BA_VDF5_7A1 = 16
                    t3_BA_VDF5_7A2 = 26.1
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 16
                    t3_BA_VDF5_7C2A = 27.9
                    t3_BA_VDF5_7C2B = 44.4
                    t3_BA_VDF5_7C3 = 27.6
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.1
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 5.3
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 0
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Lampung (Jalan Lintas Timur)' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.1
                    t3_BA_VDF5_7A1 = 27.9
                    t3_BA_VDF5_7A2 = 26.2
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 54.4
                    t3_BA_VDF5_7C2A = 15.4
                    t3_BA_VDF5_7C2B = 8.3
                    t3_BA_VDF5_7C3 = 23.2
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.8
                    t3_BA_VDF4_7A1 = 13.8
                    t3_BA_VDF4_7A2 = 12.7
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 24.2
                    t3_BA_VDF4_7C2A = 7.8
                    t3_BA_VDF4_7C2B = 5.9
                    t3_BA_VDF4_7C3 = 11.6
                elif Daerah_tinjauan == 'Nusa Tenggara Timur - Maluku - Maluku Utara - Papua Barat - Papua' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 1
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 25.5
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 0
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 0.9
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 13.2
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 0
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Nusa Tenggara Barat' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.9
                    t3_BA_VDF5_7A1 = 5.8
                    t3_BA_VDF5_7A2 = 27.3
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 5.8
                    t3_BA_VDF5_7C2A = 14.2
                    t3_BA_VDF5_7C2B = 4.4
                    t3_BA_VDF5_7C3 = 6.8
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.6
                    t3_BA_VDF4_7A1 = 3.9
                    t3_BA_VDF4_7A2 = 12.5
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 3.9
                    t3_BA_VDF4_7C2A = 7.8
                    t3_BA_VDF4_7C2B = 3
                    t3_BA_VDF4_7C3 = 4.3
                elif Daerah_tinjauan == 'Riau' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.3
                    t3_BA_VDF5_7A1 = 16
                    t3_BA_VDF5_7A2 = 26.1
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 16
                    t3_BA_VDF5_7C2A = 27.9
                    t3_BA_VDF5_7C2B = 44.4
                    t3_BA_VDF5_7C3 = 27.6
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3
                    t3_BA_VDF4_7A1 = 9.8
                    t3_BA_VDF4_7A2 = 13.6
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 9.3
                    t3_BA_VDF4_7C2A = 15.9
                    t3_BA_VDF4_7C2B = 21.2
                    t3_BA_VDF4_7C3 = 15.3
                elif Daerah_tinjauan == 'Sulawesi Barat' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 5.3
                    t3_BA_VDF5_7A1 = 10.2
                    t3_BA_VDF5_7A2 = 22.3
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 10.9
                    t3_BA_VDF5_7C2A = 2.2
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 3.2
                    t3_BA_VDF4_7A1 = 6.5
                    t3_BA_VDF4_7A2 = 11.9
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 7.1
                    t3_BA_VDF4_7C2A = 2
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Sulawesi Selatan' :
                    t3_BA_VDF4_5B = 1.3
                    t3_BA_VDF4_6A = 0.4
                    t3_BA_VDF4_6B = 2.8
                    t3_BA_VDF4_7A1 = 12.4
                    t3_BA_VDF4_7A2 = 10.2
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 10
                    t3_BA_VDF4_7C2A = 19.2
                    t3_BA_VDF4_7C2B = 12.3
                    t3_BA_VDF4_7C3 = 8.4
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2
                    t3_BA_VDF4_7A1 = 7.8
                    t3_BA_VDF4_7A2 = 6.3
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 6.9
                    t3_BA_VDF4_7C2A = 11.4
                    t3_BA_VDF4_7C2B = 7.6
                    t3_BA_VDF4_7C3 = 5.4
                elif Daerah_tinjauan == 'Sulawesi Utara' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4.7
                    t3_BA_VDF5_7A1 = 16.1
                    t3_BA_VDF5_7A2 = 26.8
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 29.1
                    t3_BA_VDF5_7C2A = 31.3
                    t3_BA_VDF5_7C2B = 0
                    t3_BA_VDF5_7C3 = 64.4
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.4
                    t3_BA_VDF4_7A1 = 9.2
                    t3_BA_VDF4_7A2 = 13.8
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 16.7
                    t3_BA_VDF4_7C2A = 16.8
                    t3_BA_VDF4_7C2B = 0
                    t3_BA_VDF4_7C3 = 31.9
                elif Daerah_tinjauan == 'Sumatera Barat Lintas Barat Pesisir Selatan' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.4
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 6.2
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 25.5
                    t3_BA_VDF5_7C2A = 11.3
                    t3_BA_VDF5_7C2B = 27.3
                    t3_BA_VDF5_7C3 = 10.3
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 13.4
                    t3_BA_VDF4_7C2A = 6.5
                    t3_BA_VDF4_7C2B = 14.5
                    t3_BA_VDF4_7C3 = 7
                elif Daerah_tinjauan == 'Sumatera Barat Lintas Barat Pesisir Utara' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.7
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 8.9
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 14.5
                    t3_BA_VDF5_7C2A = 0
                    t3_BA_VDF5_7C2B = 10.4
                    t3_BA_VDF5_7C3 = 9.1
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.9
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 5.4
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 8.7
                    t3_BA_VDF4_7C2A = 0
                    t3_BA_VDF4_7C2B = 7.8
                    t3_BA_VDF4_7C3 = 6.8
                elif Daerah_tinjauan == 'Sumatera Barat Lintas Tengah Selatan' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.6
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 16.9
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 13.6
                    t3_BA_VDF5_7C2A = 12.4
                    t3_BA_VDF5_7C2B = 26.1
                    t3_BA_VDF5_7C3 = 31.5
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.7
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 9.6
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 8.5
                    t3_BA_VDF4_7C2A = 8.8
                    t3_BA_VDF4_7C2B = 13.9
                    t3_BA_VDF4_7C3 = 17.6
                elif Daerah_tinjauan == 'Sumatera Barat Lintas Tengah Utara' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 2.8
                    t3_BA_VDF5_7A1 = 0
                    t3_BA_VDF5_7A2 = 8.7
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 11.9
                    t3_BA_VDF5_7C2A = 21.4
                    t3_BA_VDF5_7C2B = 10.1
                    t3_BA_VDF5_7C3 = 0
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 1.9
                    t3_BA_VDF4_7A1 = 0
                    t3_BA_VDF4_7A2 = 5
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 7.5
                    t3_BA_VDF4_7C2A = 12.8
                    t3_BA_VDF4_7C2B = 6.1
                    t3_BA_VDF4_7C3 = 0
                elif Daerah_tinjauan == 'Sumatera Selatan (Jalan Lintas Timur)' :
                    t3_BA_VDF5_5B = 1.3
                    t3_BA_VDF5_6A = 0.4
                    t3_BA_VDF5_6B = 4
                    t3_BA_VDF5_7A1 = 10.5
                    t3_BA_VDF5_7A2 = 16.3
                    t3_BA_VDF5_7B1 = 0
                    t3_BA_VDF5_7B2 = 0
                    t3_BA_VDF5_7C1 = 18.7
                    t3_BA_VDF5_7C2A = 18.9
                    t3_BA_VDF5_7C2B = 11.9
                    t3_BA_VDF5_7C3 = 20
                    # vdf 4
                    t3_BA_VDF4_5B = 1.2
                    t3_BA_VDF4_6A = 0.5
                    t3_BA_VDF4_6B = 2.8
                    t3_BA_VDF4_7A1 = 7.1
                    t3_BA_VDF4_7A2 = 8.8
                    t3_BA_VDF4_7B1 = 0
                    t3_BA_VDF4_7B2 = 0
                    t3_BA_VDF4_7C1 = 11.2
                    t3_BA_VDF4_7C2A = 11.4
                    t3_BA_VDF4_7C2B = 7.5
                    t3_BA_VDF4_7C3 = 11

                stabilisasi_t3__234 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr234_t3 * 0 * DD * DL)
                stabilisasi_t3__5A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr5A_t3 * 0 * DD * DL)
                stabilisasi_t3__5B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr5B_t3 * t3_BA_VDF5_5B * DD * DL)
                stabilisasi_t3__6A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr6A_t3 * t3_BA_VDF5_6A * DD * DL)
                stabilisasi_t3__6B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr6B_t3 * t3_BA_VDF5_6B * DD * DL)
                stabilisasi_t3__7A1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7A1_t3 * t3_BA_VDF5_7A1 * DD * DL)
                stabilisasi_t3__7A2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7A2_t3 * t3_BA_VDF5_7A2 * DD * DL)
                stabilisasi_t3__7B1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7B1_t3 * t3_BA_VDF5_7B1 * DD * DL)
                stabilisasi_t3__7B2 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7B2_t3 * t3_BA_VDF5_7B2 * DD * DL)
                stabilisasi_t3__7C1 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C1_t3 * t3_BA_VDF5_7C1 * DD * DL)
                stabilisasi_t3__7C2A = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C2A_t3 * t3_BA_VDF5_7C2A * DD * DL)
                stabilisasi_t3__7C2B = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C2B_t3 * t3_BA_VDF5_7C2B * DD * DL)
                stabilisasi_t3__7C3 = math.ceil(365 * ((((1 + 0.01 * i) ** 40) - 1) / (0.01 * i)) * lhr7C3_t3 * t3_BA_VDF5_7C3 * DD * DL)
                stabilisasi_t3 = (stabilisasi_t3__5B + stabilisasi_t3__6A +
                                  stabilisasi_t3__6B + stabilisasi_t3__7A1 + stabilisasi_t3__7A1 + stabilisasi_t3__7A2 +
                                  stabilisasi_t3__7B1 + stabilisasi_t3__7B2 + stabilisasi_t3__7C1 + stabilisasi_t3__7C2A +
                                  stabilisasi_t3__7C3)
                t3_e1p__234 = math.ceil(365 * 22 * lhr234_t3 * 0 * DD * DL)
                t3_e1p__5A = math.ceil(365 * 22 * lhr5A_t3 * 0 * DD * DL)
                t3_e1p__5B = math.ceil(365 * 22 * lhr5B_t3 * t3_BA_VDF4_5B * DD * DL)
                t3_e1p__6A = math.ceil(365 * 22 * lhr6A_t3 * t3_BA_VDF4_6A * DD * DL)
                t3_e1p__6B = math.ceil(365 * 22 * lhr6B_t3 * t3_BA_VDF4_6B * DD * DL)
                t3_e1p__7A1 = math.ceil(365 * 22 * lhr7A1_t3 * t3_BA_VDF4_7A1 * DD * DL)
                t3_e1p__7A2 = math.ceil(365 * 22 * lhr7A2_t3 * t3_BA_VDF4_7A2 * DD * DL)
                t3_e1p__7B1 = math.ceil(365 * 22 * lhr7B1_t3 * t3_BA_VDF4_7B1 * DD * DL)
                t3_e1p__7B2 = math.ceil(365 * 22 * lhr7B2_t3 * t3_BA_VDF4_7B2 * DD * DL)
                t3_e1p__7C1 = math.ceil(365 * 22 * lhr7C1_t3 * t3_BA_VDF4_7C1 * DD * DL)
                t3_e1p__7C2A = math.ceil(365 * 22 * lhr7C2A_t3 * t3_BA_VDF4_7C2A * DD * DL)
                t3_e1p__7C2B = math.ceil(365 * 22 * lhr7C2B_t3 * t3_BA_VDF4_7C2B * DD * DL)
                t3_e1p__7C3 = math.ceil(365 * 22 * lhr7C3_t3 * t3_BA_VDF4_7C3 * DD * DL)
                t3_e1p = (t3_e1p__5B + t3_e1p__6A +
                          t3_e1p__6B + t3_e1p__7A1 + t3_e1p__7A2 + t3_e1p__7B1 +
                          t3_e1p__7B2 + t3_e1p__7C1 + t3_e1p__7C2A + t3_e1p__7C2B + t3_e1p__7C3)
                t3_e3p__234 = math.ceil(365 * 28.2 * lhr234_t3 * 0 * DD * DL)
                t3_e3p__5A = math.ceil(365 * 28.2 * lhr5A_t3 * 0 * DD * DL)
                t3_e3p__5B = math.ceil(365 * 28.2 * lhr5B_t3 * t3_BA_VDF4_5B * DD * DL)
                t3_e3p__6A = math.ceil(365 * 28.2 * lhr6A_t3 * t3_BA_VDF4_6A * DD * DL)
                t3_e3p__6B = math.ceil(365 * 28.2 * lhr6B_t3 * t3_BA_VDF4_6B * DD * DL)
                t3_e3p__7A1 = math.ceil(365 * 28.2 * lhr7A1_t3 * t3_BA_VDF4_7A1 * DD * DL)
                t3_e3p__7A2 = math.ceil(365 * 28.2 * lhr7A2_t3 * t3_BA_VDF4_7A2 * DD * DL)
                t3_e3p__7B1 = math.ceil(365 * 28.2 * lhr7B1_t3 * t3_BA_VDF4_7B1 * DD * DL)
                t3_e3p__7B2 = math.ceil(365 * 28.2 * lhr7B2_t3 * t3_BA_VDF4_7B2 * DD * DL)
                t3_e3p__7C1 = math.ceil(365 * 28.2 * lhr7C1_t3 * t3_BA_VDF4_7C1 * DD * DL)
                t3_e3p__7C2A = math.ceil(365 * 28.2 * lhr7C2A_t3 * t3_BA_VDF4_7C2A * DD * DL)
                t3_e3p__7C2B = math.ceil(365 * 28.2 * lhr7C2B_t3 * t3_BA_VDF4_7C2B * DD * DL)
                t3_e3p__7C3 = math.ceil(365 * 28.2 * lhr7C3_t3 * t3_BA_VDF4_7C3 * DD * DL)
                t3_e3p = (t3_e3p__5B + t3_e3p__6A +
                          t3_e3p__6B + t3_e3p__7A1 + t3_e3p__7A2 + t3_e3p__7B1 +
                          t3_e3p__7B2 + t3_e3p__7C1 + t3_e3p__7C2A + t3_e3p__7C2B + t3_e3p__7C3)
                cesa4_untuktebal_t3__234 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr234_t3 * 0 * DD * DL)
                cesa4_untuktebal_t3__5A = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr5A_t3 * 0 * DD * DL)
                cesa4_untuktebal_t3__5B = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr5B_t3 * 2 * DD * DL)
                cesa4_untuktebal_t3__6A = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr6A_t3 * 2 * DD * DL)
                cesa4_untuktebal_t3__6B = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr6B_t3 * 2 * DD * DL)
                cesa4_untuktebal_t3__7A1 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7A1_t3 * 2 * DD * DL)
                cesa4_untuktebal_t3__7A2 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7A2_t3 * 2 * DD * DL)
                cesa4_untuktebal_t3__7B1 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7B1_t3 * 4 * DD * DL)
                cesa4_untuktebal_t3__7B2 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7B2_t3 * 4 * DD * DL)
                cesa4_untuktebal_t3__7C1 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7C1_t3 * 3 * DD * DL)
                cesa4_untuktebal_t3__7C2A = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7C2A_t3 * 3 * DD * DL)
                cesa4_untuktebal_t3__7C2B = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7C2B_t3 * 3 * DD * DL)
                cesa4_untuktebal_t3__7C3 = math.ceil(365 * ((((1 + 0.01 * i) ** UR) - 1) / (0.01 * i)) * lhr7C3_t3 * 3 * DD * DL)
                cesa4_untuktebal_t3 = (cesa4_untuktebal_t3__5B + cesa4_untuktebal_t3__6A +
                                       cesa4_untuktebal_t3__6B + cesa4_untuktebal_t3__7A1 + cesa4_untuktebal_t3__7A2 + cesa4_untuktebal_t3__7B1 +
                                       cesa4_untuktebal_t3__7C1 + cesa4_untuktebal_t3__7C2A + cesa4_untuktebal_t3__7C2B + cesa4_untuktebal_t3__7C3)
                total_lhr_t3 = (lhr234_t3 + lhr5A_t3 + lhr5B_t3 + lhr6A_t3 + lhr6B_t3 + lhr7A1_t3 + lhr7A2_t3 + lhr7B1_t3 + lhr7B2_t3 +
                                lhr7C1_t3 + lhr7C2A_t3 + lhr7C2B_t3 + lhr7C3_t3)
                jmlkendberat_t3 = (lhr5B_t3 + lhr6A_t3 + lhr6B_t3 + lhr7A1_t3 + lhr7A2_t3 + lhr7B1_t3 + lhr7B2_t3 +
                                lhr7C1_t3 + lhr7C2A_t3 + lhr7C2B_t3 + lhr7C3_t3)
                # Perencanaan Tebal Perkerasan Lalu
                if cesa4_untuktebal_t3 < 4300000 :
                    LB_Tebal_Perkerasan_Beton_t1 = 265
                elif 4300000 <= cesa4_untuktebal_t3 < 8600000 :
                    LB_Tebal_Perkerasan_Beton_t1 = 275
                elif 8600000 <= cesa4_untuktebal_t3 < 25800000 :
                    LB_Tebal_Perkerasan_Beton_t1 = 285
                elif 25800000 <= cesa4_untuktebal_t3 < 43000000 :
                    LB_Tebal_Perkerasan_Beton_t1 = 295
                elif cesa4_untuktebal_t3 >= 43000000 :
                    LB_Tebal_Perkerasan_Beton_t1 = 305

                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas' :
                    beban_lalin_t3 = t3_e1p
                elif deskripsi_jalan == 'Jalan kecil dua arah' :
                    beban_lalin_t3 = t3_e1p
                elif deskripsi_jalan == 'Jalan lokal' :
                    beban_lalin_t3 = t3_e1p
                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry' :
                    beban_lalin_t3 = t3_e3p
                elif deskripsi_jalan =='Jalan kolektor':
                    beban_lalin_t3 = t3_e3p
                def diamater_dowel_t3() :
                    if 265 <= LB_Tebal_Perkerasan_Beton_t1 <= 275 :
                        d_dowel = 32
                        return d_dowel
                    elif 285 <= LB_Tebal_Perkerasan_Beton_t1 <= 305 :
                        d_dowel = 40
                        return d_dowel
                def diamater_tiebar_t3() :
                    luas_penampang_tulangan = 204 * (LB_Tebal_Perkerasan_Beton_t1 / 1000) * lebar_lajur
                    if luas_penampang_tulangan <= 201 :
                        diamater_tiebar = 16
                        return diamater_tiebar
                    elif 201 < luas_penampang_tulangan <= 284 :
                        diamater_tiebar = 19
                        return diamater_tiebar
                    elif 284 < luas_penampang_tulangan <= 380 :
                        diamater_tiebar = 22
                        return diamater_tiebar
                    elif 380 < luas_penampang_tulangan <= 491 :
                        diamater_tiebar = 25
                        return diamater_tiebar
                    elif 491 < luas_penampang_tulangan <= 661 :
                        diamater_tiebar = 29
                        return diamater_tiebar
                    elif 661 < luas_penampang_tulangan <= 804 :
                        diamater_tiebar = 32
                        return diamater_tiebar
                    elif 804 < luas_penampang_tulangan <= 1018 :
                        diamater_tiebar = 36
                        return diamater_tiebar
                    elif 1018 < luas_penampang_tulangan <= 1257 :
                        diamater_tiebar = 40
                        return diamater_tiebar
                    elif 1257 < luas_penampang_tulangan <= 1964 :
                        diamater_tiebar = 50
                        return diamater_tiebar
                    elif 1964 < luas_penampang_tulangan <= 2290 :
                        diamater_tiebar = 54
                        return diamater_tiebar
                    elif 2290 < luas_penampang_tulangan <= 2552 :
                        diamater_tiebar = 57
                        return diamater_tiebar
                def panjang_batang_pengikat_t3() :
                    panjang_batang_pengikat = (38.3 * diamater_tiebar_t3()) + 75
                    return panjang_batang_pengikat
                def lalin_berat_t3() :    
                    df_tebal_perkerasan = pd.DataFrame(
                        {
                            "Parameter" : [
                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)", "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                "Lalu Lintas (Berat/Rendah)", "Komulatif Kelompok Sumbu Kendaraan Berat", "Menggunakan Bahu Pelat Beton",
                                "Tebal Perkerasan Beton (mm)", "Diameter Dowel (mm)" , "Panjang Dowel (mm)", "Jarak Antar Dowel (mm)",
                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "Lapis Fondasi LMC (mm)",
                                "Lapis Dainase (mm)"
                            ],
                            "Hasil" : [
                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr_t3), (beban_lalin_t3), ("Berat"),
                                (cesa4_untuktebal_t3), 
                                ("Ya"), (LB_Tebal_Perkerasan_Beton_t1), (diamater_dowel_t3()), ("450"), ("300"),
                                (diamater_tiebar_t3()), round(panjang_batang_pengikat_t3(), 3), ("750"),("100"), ("150")
                            ]
                        }
                    )
                    return st.dataframe(df_tebal_perkerasan) 

                def lalin_rendah_t3() :
                    keadaan_tanah_dasar = st.selectbox("Tanah Dasar",['Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton',
                                                                'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton',
                                                                'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton',
                                                                'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton'])
                    if keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Dengan Pelat Beton' :
                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                        bahu_jalan = "Ya"
                        tulangan_distribusi_retak = "Ya"
                        if jmlkendberat_t3 == 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                            dapat_dilalui_truk = "Tidak"
                        elif jmlkendberat_t3 > 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah= 180
                            dapat_dilalui_truk = "Ya"
                    elif keadaan_tanah_dasar == 'Tanah Lunak Dengan Lapis Penopang dan Bahu Jalan Bukan Pelat Beton' :
                        tanah_dasar = "Tanah Lunak Dengan Lapis Penopang"
                        bahu_jalan = "Tidak"
                        tulangan_distribusi_retak = "Ya"
                        if jmlkendberat_t3 == 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                            dapat_dilalui_truk = "Tidak"
                        elif jmlkendberat_t3 > 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 200
                            dapat_dilalui_truk = "Ya"
                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Dengan Pelat Beton' :
                        tanah_dasar = "Dipadatkan Normal"
                        bahu_jalan = "Ya"
                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                        if jmlkendberat_t3 == 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 135
                            dapat_dilalui_truk = "Tidak"
                        elif jmlkendberat_t3 > 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 160
                            dapat_dilalui_truk = "Ya"
                    elif keadaan_tanah_dasar == 'Dipadatkan Normal dan Bahu Jalan Bukan Pelat Beton' :
                        tanah_dasar = "Dipadatkan Normal"
                        bahu_jalan = "Tidak"
                        tulangan_distribusi_retak = "Ya Jika Daya Dukung Fondasi Tidak Seragam"
                        if jmlkendberat_t3 == 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 150
                            dapat_dilalui_truk = "Tidak"
                        elif jmlkendberat_t3 > 0 :
                            LR_Tebal_Perkerasan_Beton_Rendah = 175
                            dapat_dilalui_truk = "Ya"
                    df_tebal_perkerasan = pd.DataFrame(
                        {
                            "Parameter" : [
                                "Faktor Pengali Pertumbuhan Lalu Lintas Kumulatif", "Lalu Lintas Harian Rata-Rata (Kendaraan/Hari)",
                                "Beban Lalu Lintas Desain (Aktual) (ESA4)",
                                "Lalu Lintas (Berat/Rendah)", "Tanah Dasar", "Menggunakan Bahu Pelat Beton", "Dapat Dilalui Truk",
                                "Tebal Perkerasan Beton (mm)", "Tulangan Distribusi Retak", "Dowel" ,
                                "Diameter Tie Bar (mm)", "Panjang Tie Bar Minimum (mm)", "Jarak Antar Tie Bar (mm)", "LMC (mm)",
                                "Lapis Fondasi Kelas A (Ukuran Butir Nominal Maksimum 30 mm) (mm)", "Jarak Sambungan Melintang (m)"
                            ],
                            "Hasil" : [
                                round(faktor_pengali_pertumbuhan_lalu_lintas, 3), (total_lhr_t3), (beban_lalin_t3), ("Rendah"), 
                                (tanah_dasar), (bahu_jalan), (dapat_dilalui_truk),
                                (LR_Tebal_Perkerasan_Beton_Rendah), (tulangan_distribusi_retak), ("Tidak Dibutuhkan"), 
                                (diamater_tiebar_t3()), round(panjang_batang_pengikat_t3(), 3), ("750"), ("Tidak Dibutuhkan"),
                                ("125"), ("4")
                            ]
                        }
                    )
                    return st.dataframe(df_tebal_perkerasan)

                menghitung_cbr_t3 = st.checkbox("Input Data CBR")
                with tabs3:
                    if menghitung_cbr_t3 :
                        st.write("Format file excel harus sesuai dengan template yang telah disediakan berikut")
                        with open("template.xlsx", "rb") as file:
                            btn = st.download_button(
                                    label="Download File Excel",
                                    data=file,
                                    file_name="template.xlsx",
                                    mime="xlsx")

                        ## ------ UPLOAD FILE EXCEL
                        upload_file_excel = st.file_uploader('Masukkan Data CBR Dalam Format xlsx', type='xlsx')
                        if upload_file_excel :
                            st.markdown('---')
                            df = pd.read_excel(upload_file_excel, engine='openpyxl')
                            st.write("Data awal :")
                            st.dataframe(df)
                            staberapa = df['STA']
                            nilaicbr = df['NILAI CBR']
                            koefvar=fkoefvar(df)
                            rata2=df["NILAI CBR"].mean()
                            nstd=df["NILAI CBR"].std()
                            jumlahdata=len(df)
                            df_data_awal = pd.DataFrame(
                                            {
                                                "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi"],
                                                "Hasil" : [(jumlahdata), (rata2), (nstd), (koefvar)]
                                            }
                                        )
                            st.dataframe(df_data_awal)
                            if (koefvar < 30) or (jumlahdata <=10):
                                st.success("Dapat dijadikan satu segemen")
                            else :
                                st.warning("Tidak dapat dijadikan satu segemen")
                            
                            rumus_cbr_karakteristik = st.selectbox("Rumus CBR Karakteristik",['Metode distribusi normal standar',
                                                                                            'Metode persentil',])
                            if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                                pilih_tipe_jalan = st.radio("Tipe Jalan",['Bebas Hambatan', 'Jalan Kolektor atau Arteri', 'Jalan Lokal dan Jalan Kecil'])
                                if pilih_tipe_jalan == 'Jalan Kolektor atau Arteri':
                                    f_nilai = 1.282
                                elif pilih_tipe_jalan == 'Bebas Hambatan':
                                    f_nilai = 1.645
                                elif pilih_tipe_jalan == 'Jalan Lokal dan Jalan Kecil':
                                    f_nilai = 0.842

                            jumlah_segmen = int(st.number_input("Input jumlah segmen :",1))
                            # List untuk menyimpan jumlah data per list yang diinput oleh pengguna
                            data_per_list = []
                            # Memasukkan jumlah data per list sesuai jumlah list yang diinginkan
                            ukuran_bagian=(jumlahdata//jumlah_segmen)
                            junlahdataterambil=ukuran_bagian*jumlah_segmen
                            bagian = []
                            startdata = 0
                            for i in range(jumlah_segmen-1):
                                enddata = min(startdata + ukuran_bagian, jumlahdata)
                                bagian.append(df.iloc[startdata:enddata])
                                startdata=enddata
                            bagian.append(df.iloc[startdata:jumlahdata])
                            statussegmen=False
                            for i in range(jumlah_segmen):
                                jml_data_persegmen = len(bagian[i])
                                data = st.number_input(f"Masukkan banyak data CBR untuk segmen {i+1}", min_value=1, value=jml_data_persegmen)
                                data_per_list.append(data)

                            # Memunculkan hasil pembagian data pada list
                            if st.button("Tampilkan"):
                                if len(df) > 0:
                                    lists = divide_into_lists(df, data_per_list)
                                    for i, lst in enumerate(lists, start=1):
                                        jumlah_banyak_data_cbr = len(lst)
                                        st.write(f"Segmen ke-{i} dengan jumlah data {jumlah_banyak_data_cbr} dapat dilihat pada tabel berikut :")
                                        st.dataframe(lst)
                                        Nilai_cbr_rata2 = cbr_rata2(lst)
                                        nilai_devstandar = nilai_std(lst)
                                        koefvar=fkoefvar(lst)
                                        if len(lst)>10 and koefvar>30:
                                            statussegmen=True
                                        else :
                                            statussegmen=False
                                        if jumlah_banyak_data_cbr <= 10:
                                            nilai_terkecil_cbr = min((lst["NILAI CBR"]))
                                            cbr_karakteristik = nilai_terkecil_cbr
                                        else :
                                            if rumus_cbr_karakteristik == 'Metode distribusi normal standar' :
                                                cbr_karakteristik = Nilai_cbr_rata2 - f_nilai * nilai_devstandar
                                            else :
                                                xdata=(lst["NILAI CBR"])
                                                cbr_karakteristik = np.percentile(xdata, 10)
                                        ## -STABILISASI TANAH
                                        if  cbr_karakteristik < 1:
                                            nilai_stabilisasi = "Perlu penangan lebih lanjut"
                                        elif  1 <= cbr_karakteristik < 2.5:
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = 1000
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = 1100
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = 1200
                                        elif  2.5 <= cbr_karakteristik < 3:
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = 175
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = 250
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = 350
                                        elif 3 <= cbr_karakteristik < 4 :
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = 150
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = 200
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = 300
                                        elif 4 <= cbr_karakteristik < 5 :
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = 100
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = 150
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = 200
                                        elif 5 <= cbr_karakteristik < 6 :
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = 100
                                        elif cbr_karakteristik >= 6 :
                                            if stabilisasi_t3 < 2000000 :
                                                nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                            elif 2000000 <= stabilisasi_t3 <= 4000000 :
                                                nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                            elif stabilisasi_t3 > 4000000 :
                                                nilai_stabilisasi = "Tidak diperlukan perbaikan"
                                        ## --TABEL HASIL
                                        df_hasil_stabilisasi = pd.DataFrame(
                                            {
                                                "Nama" : ["Jumlah Data CBR", "Rata-Rata Nilai CBR", "Deviasi Standar", "Koefisien Variasi", "CBR Karakteristik",
                                                        "Beban lalu lintas pada lajur rencana dengan umur rencana 40 tahun (juta ESA5)" ,
                                                        "Tebal Minimum Material Timbunan Pilihan (mm)", "Stabilisasi Diatas Material Timbunan Pilihan (mm)"],
                                                "Hasil" : [(jumlah_banyak_data_cbr), round(Nilai_cbr_rata2, 3), round(nilai_devstandar, 3), round(koefvar, 3), 
                                                        round(cbr_karakteristik, 3), (stabilisasi_t3), (nilai_stabilisasi), ("150")]
                                            }
                                        )
                                        st.dataframe(df_hasil_stabilisasi)
                                        # st.warning(koefvar)
                                        if statussegmen:
                                            st.warning("Sebaiknya dibagi segmen lagi")
                                        else:
                                            st.success(f"Segmen {i} memenuhi")

                        with tabs4 :
                            menghitung_tebal_t3 = st.checkbox("Hitung Tebal Perkerasan")
                            if menghitung_tebal_t3 :
                                if deskripsi_jalan == 'Jalan desa minor dengan akses kendaraan berat terbatas' :
                                    if t3_e1p > 45000 :
                                        lalin_berat_t3()
                                    else :
                                        lalin_rendah_t3()
                                elif deskripsi_jalan == 'Jalan kecil dua arah' :
                                    if t3_e1p > 70000 :
                                        lalin_berat_t3()
                                    else :
                                        lalin_rendah_t3()
                                elif deskripsi_jalan == 'Jalan lokal' :
                                    if t3_e1p > 800000 :
                                        lalin_berat_t3()
                                    else :
                                        lalin_rendah_t3()
                                elif deskripsi_jalan == 'Akses lokal daerah industri atau quarry' :
                                    if t3_e3p > 1500000 :
                                        lalin_berat_t3()
                                    else :
                                        lalin_rendah_t3()
                                elif deskripsi_jalan == 'Jalan kolektor' :
                                    if t3_e3p > 5000000 :
                                        lalin_berat_t3()
                                    else :
                                        lalin_rendah_t3()