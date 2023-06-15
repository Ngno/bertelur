import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

def main():
    # Set page configuration
    st.set_page_config(page_title="Stunting dan Telurnya", layout="wide")

    # Set app title and description
    st.markdown("Data Story")
    st.title("STUNTING DAN TELURNYA")
    st.markdown("Menilik Gambaran Konsumsi Telur di Zona Merah Stunting")

    # Add navigation sidebar
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Go to", ["Data Story", "About", "Survey"])

    # Home page
    if menu_selection == "Data Story":
      #  st.header("Chapter I: Data Pengantar")
        st.subheader("A. Tentang Stunting")
        st.write("Stunting adalah status kekurangan gizi kronis pada balita yang ditandai dengan Tinggi Badan per Umur (TB/U) < -2 SD pada kurva pertumbuhan WHO. Masa balita termasuk 1000 hari pertama kehidupan adalah masa yang sangat krusial. Keterlambatan tumbuh kembang hingga gagal tumbuh pada masa ini berdampak negatif pada perkembangan otak, dan meningkatkan risiko berbagai penyakit kronis saat dewasa.")      
    # insert table image. 
        st.image("tbu.jpg")
        st.write("Gambar 1. Tabel standar Panjang atau Tinggi Badan per Umur untuk balita laki-laki. Kategori stunting adalah -2SD hingga -3SD (Pendek), dan <-3SD (Sangat Pendek)")

        # Show grafik Penurunan angka stunting di Indonesia tahun 2017-2022/2023
        tahun = [2016,2017,2018,2019,2021,2022]
        stunting = [27.5,29.6,30.8,27.7,24.4,21.6]

        # Adjust the figure size
        fig, ax = plt.subplots(figsize=(6, 4))  # Set the width and height in inches
    
         # Create the plot using matplotlib
        ax.plot(tahun, stunting, marker='o')
        ax.set_xlabel('Tahun')
        ax.set_ylabel('Prevalensi Stunting  (%)')
        ax.set_title('Perubahan Prevalensi Stunting di Indonesia (2016-2022)')
    
        # Set the y-axis range and tick marks
        ax.set_ylim(0, 50)
        ax.set_yticks(range(0, 51, 10))

        # Add value annotations to each point
        for i, j in zip(tahun, stunting):
            ax.text(i, j, f'{j}', ha='center', va='bottom', fontsize=8)  

        # Display the plot using st.pyplot()
        st.pyplot(fig)
        
        #caption
        st.write("Gambar 2. Grafik perubahan prevalensi stunting nasional dari tahun 2016-2022.Dari berbagai sumber")

        # Data stunting semua provinsi di Indonesia tahun 2022 bar chart
        # Data
        # Data
        stunting2022 = [35.3, 35.0, 34.6, 32.7, 31.2, 30.0, 28.2, 27.8, 27.7, 27.2, 26.9, 26.1, 26.1, 25.2, 24.6, 23.9, 23.8, 22.1, 21.6, 21.1, 20.8, 20.5, 20.2, 20.0, 19.8, 19.2, 18.6, 18.5, 18.0, 17.0, 16.4, 15.4, 15.2, 14.8, 8.0]
        provinsi2022 = [
        'Nusa Tenggara Timur', 'Sulawesi Barat', 'Papua', 'Nusa Tenggara Barat', 'Aceh', 'Papua Barat', 'Sulawesi Tengah', 
        'Kalimantan Barat', 'Sulawesi Tenggara', 'Sulawesi Selatan', 'Kalimantan Tengah', 'Maluku Utara', 'Maluku', 
        'Sumatera Barat', 'Kalimantan Selatan', 'Kalimantan Timur', 'Gorontalo', 'Kalimantan Utara', 'INDONESIA', 
        'Sumatera Utara', 'Jawa Tengah', 'Sulawesi Utara', 'Jawa Barat', 'Banten', 'Bengkulu', 'Jawa Timur', 
        'Sumatera Selatan', 'Kep. Bangka Belitung', 'Jambi', 'Riau', 'DI Yogyakarta', 'Kepulauan Riau', 'Lampung', 
        'DKI Jakarta', 'Bali']
     
       # Sort the data
        sorted_data = sorted(zip(provinsi2022, stunting2022), key=lambda x: x[1], reverse=True)
        provinsi2022_sorted, stunting2022_sorted = zip(*sorted_data)

        # Assign colors based on stunting values
        colors = []
        for provinsi, value in zip(provinsi2022, stunting2022):
            if provinsi == 'INDONESIA':
                colors.append('purple')  # Custom color for Indonesia
            elif value > 30:
                colors.append('red')
            elif value >= 20:
                colors.append('yellow')
            elif value >= 10:
                colors.append('green')
            else:
                colors.append('blue')

        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create horizontal bar chart
        bars = ax.barh(provinsi2022_sorted, stunting2022_sorted, color=colors)

        # Add value labels to the bars with rotated labels
        for bar, height in zip(bars, stunting2022_sorted):
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2, f'{height}', ha='left', va='center', rotation=0, fontsize=9)
        # Customize the plot
        ax.set_xlabel('Prevalensi Stunting (%)',fontsize=12)
        ax.set_title('Prevalensi Stunting per Provinsi di Indonesia Tahun 2022')

        # Adjust figure size
        fig.set_size_inches(10, len(provinsi2022_sorted) * 0.4)

        # Reverse the y-axis to display highest values at the top
        ax.invert_yaxis()

        # Show the plot
        st.pyplot(fig)

        #caption
        st.write("Gambar 3. Grafik prevalensi stunting per provinsi di Indonesia tahun 2022 yang digolongkan menjadi empat kategori berdasarkan angka prevalensi: Zona Merah: >30%, Zona Kuning: 20%-30%, Zona Hijau: 10%-20%, dan Zona Biru: 10%. Sumber: SSGI 2022")

        st.write("Hasil dari Survey Status Gizi Indonesia tahun 2022 menunjukkan bahwa prevalensi stunting di Indonesia berada di angka 21,6 % menurun dari tahun ke tahun, namun masih di atas standar WHO, yakni 20%. Dari gambar 3 dapat diketahui bahwa ada lima provinsi di Indonesia yang masuk Zona Merah, yakni Nusa Tenggara Timur (NTT), Sulawesi Barat, Papua, Nusa Tenggara Barat (NTB), dan Aceh. Sedangkan lima provinsi dengan angka prevalensi stunting terendah adalah Bali, DKI Jakarta, Lampung, Kepulauan Riau, dan DI Yogyakarta, yangmana hanya Bali yang masuk Zona Biru.")
        st.write("Seperti masalah kesehatan lainnya, stunting adalah masalah yang kompleks. Faktor risiko yang mempengaruhi kejadian stunting termasuk : kemiskinan, status gizi ibu, pendidikan orangtua, akses fasilitas kesehatan, sanitasi dan higienitas, dll. Kompleksnya masalah yang menyertai, membuat Indonesia harus berjuang keras untuk keluar dari lingkaran setan dalam bidang kesehatan tersebut. Mengejar target dan keseriusan komitmen Sustainable Development Goals (SDGS) 2024 program penanganan stunting menjadi program Top Priority pemerintah. Salah satu caranya adalah dengan menggalakan program makan telur.")
  
        #Data konsumsi protein dan kalori per provinsi
        st.subheader("B. Ada Apa dengan Telur?")
        st.write("Telur adalah bahan pangan sumber protein dan lemak hewani, termasuk berbagai asam amino esensial yang penting untuk pembentukan sel tubuh. Telur dipilih sebagai bahan penakluk stunting dibanding sumber protein hewani lainnya karena: ")
        st.write(" - Kandungan gizinya berlimpah")
        st.write(" - Harga jauh lebih terjangkau")
        st.write(" - Relatif mudah didapatkan")
        st.write(" - Pengolahannya lebih cepat dan mudah")

        #pie chart konsumsi telur

        st.write("Pada bulan September 2022 lalu, Badan Pusat Statistik (BPS) menerbitkan hasil survey konsumsi telur per kapita per minggu tahun 2022. Jenis telur yang dikonsumsi oleh masyarakat meliputi : Telur ayam ras', 'Telur ayam kampung','Telur itik/telur itik manila','Telur lainnya (telur puyuh, telur asin mentah maupun matang, telur penyu, telur angsa, dsb)'")
        
        #TELUR ANALISA STARTS HERE
        #metrix rata2 konsumsi telur seluruh provinsi as one
        telur_dataset = "Dataset konsumsi telur perkapita seminggu 2022.xlsx"
        # Read the Excel file with column name in row 3
        df = pd.read_excel(telur_dataset, header=2)

                # Fill missing values and "-" with NaN
        # Fill missing values in 'PROVINSI' column with an empty string
        df.replace({'-': np.nan}, inplace=True)
        df['PROVINSI'].fillna('', inplace=True)

        # Convert numeric columns in object type to float type
        object_columns = df.select_dtypes(include=['object']).columns
        numeric_columns = object_columns[~object_columns.isin(['PROVINSI', 'Kabupaten/Kota'])]

        df[numeric_columns] = df[numeric_columns].astype(float)

        # Exclude the specified columns
        susu_columns = ['Susu cair pabrik', 'Susu kental manis', 'Susu bubuk', 'Susu bubuk bayi', 'Susu lainnya dan hasil lain dari susu']
        telur_columns = [col for col in df.columns if col not in susu_columns]

        # Exclude the "Kabupaten/Kota" and "PROVINSI" columns from the aggregation
        columns_to_agg = [col for col in telur_columns if col not in ['Kabupaten/Kota', 'PROVINSI']]

        # Group the DataFrame by "PROVINSI" and calculate the minimum, maximum, and average for the selected columns
        df_telurs_provinsi = df.groupby('PROVINSI')[columns_to_agg].agg(['mean'])


        #Sum up all of telurs type

        # Sum up the mean values across the telur columns for each province
        df_telur_provinsi = df_telurs_provinsi.sum(axis=1)

        # Rename the resulting series column to 'Rata-rata Konsumsi Telur'
        df_telur_provinsi = df_telur_provinsi.rename('Rata-rata Konsumsi Telur')

        # Convert the series to a DataFrame and reset the index
        df_telur_provinsi = df_telur_provinsi.reset_index()

        # Sort the DataFrame by the 'Rata-rata Konsumsi Telur' column in ascending order
        df_telur_provinsi = df_telur_provinsi.sort_values(by='Rata-rata Konsumsi Telur')

        #VISUALISATION
        # Create a bar chart using df telur provinsi
        # add Indonesia as overall mean value
        # Sort the DataFrame by the 'Mean Consumption' column in ascending order
        # Create a bar chart using the DataFrame
        
        fig, ax = plt.subplots()
        ax.bar(df_telur_provinsi['PROVINSI'], df_telur_provinsi['Rata-rata Konsumsi Telur'], color='blue')
        ax.set_xlabel('Provinsi')
        ax.set_ylabel('Rata-rata Konsumsi (Butir)')
        ax.set_title('Rata-rata Konsumsi Telur Per Kapita Per Minggu, Tahun 2022')
        ax.tick_params(axis='x', rotation=90, labelsize=8)  # Rotate x-axis labels by 90 degrees and decrease font size

        # Display the chart using Streamlit 
        st.pyplot(fig)

        
        st.write("Gambar 4. Gambaran konsumsi telur per provinsi. Dari grafik di atas dapat diketahui bahwa NTT, Papua, dan Sulawesi Barat menjadi provinsi Zona Merah Stunting yang rata-rata konsumsi telur per kapita < 2 butir per minggu. Sementara Aceh dan NTB sudah berada di angka konsumsi >2 butir.")
        
       #Produksi telur
          # Load data
        produksi_telur_dataset = "Data Produksi Telur Ayam Petelur menurut Provinsi 2022.xlsx"
        df_produksi_telur = pd.read_excel(produksi_telur_dataset)

       
       # Sort the dataframe by the production column in ascending order
        df_produksi_telur_sorted = df_produksi_telur.sort_values('2022', ascending=True)

        # Create a vertical bar chart using Plotly Express
        fig = px.bar(df_produksi_telur_sorted, x='PROVINSI', y='2022', orientation='v', hover_data=['2022'],
                    labels={'2022': 'Production'}, text='2022')

        # Set the title of the chart
        fig.update_layout(title='Produksi Telur per Provinsi Tahun 2022')

        # Configure the axis labels
        fig.update_xaxes(title='Provinsi')
        fig.update_yaxes(title='Jumlah Produksi Telur (Ton)')

        # Add custom hovertemplate to display value labels
        fig.update_traces(hovertemplate='<b>%{x}</b><br><br>Production: %{hovertext}')

        # Display the chart using Streamlit
        st.plotly_chart(fig)

        st.write("Gambar 5. Produksi telur per provinsi pada tahun 2022. Dapat diketahui provinsi-provinsi penghasil telur terbanyak mayoritas ada di pulau Jawa dan Sumatera.")

        st.write("Gambar 5 secara tidak langsung menunjukkan provinsi-provinsi yang menjadi pusat produksi hasil peternakan. Dari data tersebut juga diketahui bahwa provinsi yang berada di Zona Merah Stunting saat ini (NTT, Sulawesi Barat, Papua, NTB, dan Aceh) memproduksi telur ayam sekitar 541-40.000 Ton saja sepanjang tahun 2022. Dibandingkan dengan DI Yogyakarta dan Bali yang memiliki luas wilayah yang kecil dan status prevalensi stunting yang cukup baik, kedua daerah ini memproduksi telur masing-masing sebanyak 168.303 dan 176.855 Ton. Rendahnya produksi telur dalam provinsi dapat membuat harga telur di pasaran setempat lebih tinggi dibanding daerah utama penghasil telur akibat bertambahnya biaya produksi, terutama biaya transportasi. Harga yang semakin mahal dikhawatirkan akan menurunkan kejangkauannya dari masyarakat, sehingga konsumsi telur dan protein berkurang.")
        #Correlation of produksi and konsumsi telur daerah             
        # Sort df_telur_provinsi by province in ascending order
        df_telur_provinsi_sorted = df_telur_provinsi.sort_values(by='PROVINSI')

        # Convert the average egg consumption from per week to per month
        df_telur_provinsi_sorted['Rata-rata Konsumsi Telur'] *= 4

        # Set the figure size
        fig, ax = plt.subplots(figsize=(12, 6))

        # Set the bar width
        bar_width = 0.35

        # Set the positions of the bars on the x-axis
        x = df_produksi_telur_sorted['PROVINSI']

        # Plot the bar chart for egg production
        ax.bar(x, df_produksi_telur_sorted['2022'], width=bar_width, label='Produksi Telur per Bulan (Juta Ton)')

        # Plot the bar chart for average egg consumption
        ax.bar(x, df_telur_provinsi_sorted['Rata-rata Konsumsi Telur'], width=bar_width, label='Konsumsi Telur per Bulan')

        # Set the x-axis label and rotate the x-axis tick labels for better visibility
        ax.set_xlabel('Nama Provinsi')
        ax.set_xticklabels(x, rotation=90)

        # Set the y-axis label
        ax.set_ylabel('Kuantitas')

        # Set the chart title
        ax.set_title('Konsumsi Telur vs Produksi Telur per Daerah')

        # Add a legend
        ax.legend()

        # Display the plot
        plt.show()
                        
                
        # Load the consumption data
        df_konsumsi_telur = df_telur_provinsi

       
        # Merge the consumption and production tables on Province
        df_merged = pd.merge(df_konsumsi_telur, df_produksi_telur, on='PROVINSI')

        # Calculate the correlation between egg consumption and production
        correlation = df_merged['Rata-rata Konsumsi Telur'].corr(df_merged['2022'])
        print("Korelasi:", correlation)

        # Create a scatter plot
        fig, ax = plt.subplots()
        ax.scatter(df_merged['Rata-rata Konsumsi Telur'], df_merged['2022'])
        ax.set_xlabel('Konsumsi Telur per Butir per Minggu ')
        ax.set_ylabel('Produksi Telur (Juta Ton) per Bulan')
        ax.set_title('Hubungan antara Konsumsi dan Produksi Telur per Provinsi pada tahun 2022')

        # Display the plot using Streamlit
        st.pyplot(fig)
        
        st.write("Gambar 6. Gambaran sebaran angka konsumsi telur dihubungkan dengan angka produktivitas telur tiap provinsi")

        st.write("Plot antara konsumsi telur dan produksi telur daerah di atas menunjukkan bahwa mayoritas penduduk yang mengkonsumsi telur rata-rata 2 butir per minggu berada di provinsi yang produksi telurnya lebih tinggi. Serta, semua penduduk yang mengkonsumsi telur <2 butir per minggu berada di wilayah dengan produksi telur yang rendah. Hal ini perlu menjadi perhatian pemerintah, untuk meningkatkan produksi telur ayam di Zona Merah Stunting. Dengan adanya peningkatan produksi, diharapkan dapat menekan harga komoditas telur sehingga dapat lebih dijangkau masyarakat.")
        st.subheader("Saran")
        st.write("1. Pemerintah diharapkan dapat melakukan upaya peningkatan produktivitas ternak dan hasil ternak dengan membawa program pemberdayaan masyarakat miskin. Misal, pemerintah dapat mengalihkan bantuan telur dengan pemberdayaan masyarakat melalui usaha ternak ayam yang mana hasilnya dijual ke masyarakat dengan harga jauh lebih murah, serta merekrut pekerja dari warga miskin sekitar.")
        st.write("2. Peningkatan skill dan pemanfaatan peluang masyarakat melalui pelatihan pertanian dengan memanfaat limbah ternak yang ada. Misal, pemanfaatan kotoran ternak sebagai pupuk.")
        st.write("3. Peningkatan edukasi dan konseling pada ibu dan calon ibu mengenai pentingnya konsumsi makanan bergizi, salah satunya dengan mengkonsumsi telur. Pemberian edukasi kesehatan dan gizi seimbang dapat dimulai dari tingkat sekolah hingga warga masyarakat, termasuk remaja dan anak-anak.")
        st.write("4. Peningkatan kualitas dan ketersediaan serta pembaruan data yang dapat diakses oleh masyarakat. Termasuk komitmen menyediakan data yang jujur apa adanya. Hal ini berguna untuk meningkatkan peranan swasta dan akademisi dalam menganalisa program dan kinerja guna menangani masalah stunting bersama-sama.")


                
    # About page
    elif menu_selection == "About":
        st.header("A. Source and Refference")
        st.write("stunting.go.id")
        st.write("bps.go.id")
        st.write("https://sehatnegeriku.kemkes.go.id/baca/rilis-media/20230125/3142280/prevalensi-stunting-di-indonesia-turun-ke-216-dari-244/")
        st.write("Buku saku hasil Survey Status Gizi Indonesia 2022")
        st.header("B. Tool and Method")
        st.write("1. Data Preparation:")
        st.write("Microsoft Excel")
        st.write("Jupyter Notebook")
        st.write("DBeaver")
        st.write("2. Data Processing:")
        st.write("Python: openpyxl, Pandas, Numpy,")
        st.write("3. Data Visualisation:")
        st.write("Python: Matplotlib")
        st.write("Streamlit: pyplot ")
        st.write("4. Dashboard and Deployment:")
        st.write("Streamlit, GitHub")
    
   
    # Footer
    st.markdown("")
    st.write("Anggi Novitasari © 2023")

if __name__ == "__main__":
    main()

