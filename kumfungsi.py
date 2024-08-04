import streamlit as st

def cbr_rata2(df):
    rata2=df["NILAI CBR"].mean()
    return rata2
def nilai_std(df):
    nilai_std=df["NILAI CBR"].std()
    return nilai_std
def fkoefvar(df):
    rata2=df["NILAI CBR"].mean()
    nstd=df["NILAI CBR"].std()
    koefisien_variasi=(nstd/rata2)*100
    return koefisien_variasi
def fkoefvarbaru(segmen):
    st.success("data")
    st.dataframe(segmen)
    rata2baru=segmen["NILAI CBR"].mean()
    st.write("rata2 =",rata2baru)
    nstdbaru=segmen["NILAI CBR"].std()
    koefisien_variasi_baru=(nstdbaru/rata2baru)*100
    return koefisien_variasi_baru

def cari_nilai_terkecil(daftar):
    nilai_terkecil = daftar[0]  # Asumsikan elemen pertama sebagai nilai terkecil awal
    for nilai in daftar:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

def divide_into_lists(data_list, data_per_list):
    lists = []
    idx = 0

    # Membagi data berdasarkan jumlah data per list yang diinputkan oleh pengguna
    for num_data in data_per_list:
        current_list = data_list[idx:idx + num_data]
        lists.append(current_list)
        idx += num_data

    return lists



