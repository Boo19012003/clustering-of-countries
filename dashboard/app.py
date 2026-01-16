import streamlit as st
import pandas as pd
import plotly.express as px

# Dataset
drive_url_1 = f"https://drive.google.com/uc?id=19F2bC66Zv7b8GdAjGOz_WM86KitzMqZ2&export=download"
drive_url_2 = f"https://drive.google.com/uc?id=1YwrpOMqB6o0pxwT095dl3xGFooYR4WAL&export=download"
drive_url_3 = f"https://drive.google.com/uc?id=1XSCbVwa0M4Zim4SJy2BuMFuvh8mbx9Pj&export=download"


df_1 = pd.read_csv(drive_url_1)
df_2 = pd.read_csv(drive_url_2)
df_3 = pd.read_csv(drive_url_3)

cluster_mapping = {
    '1': 'Kém phát triển',
    '2': 'Phát triển',
    '0': 'Đang phát triển'
}

df_1['Cluster'] = df_1['Cluster'].astype(str).map(cluster_mapping)
df_2['Cluster'] = df_2['Cluster'].astype(str).map(cluster_mapping)
df_3['Cluster'] = df_3['Cluster'].astype(str).map(cluster_mapping)


# Streamlit App
st.set_page_config(
    layout="wide"
)

if 'dataset' not in st.session_state:
    st.session_state.dataset = "A"

st.markdown(
    """
    <h1 style='text-align: center; color: #90e0ef;'>
    Phân cụm quốc gia toàn cầu dựa trên các chỉ số phát triển bền vững
    </h1>
    <p style='text-align: center;'>
    Ứng dụng này hiển thị bản đồ phân cụm quốc gia toàn cầu dựa trên các chỉ số phát triển bền vững sử dụng ba phương pháp phân cụm khác nhau: GMM, KMeans và Hierarchical Clustering.
    </p>
    """, unsafe_allow_html=True
)


cols = st.columns(7, gap="small")

with cols[2]:
    if st.button("GMM Clustering", width='stretch'):
        st.session_state.dataset = "A"

with cols[3]:
    if st.button("KMeans Clustering", width='stretch'):
        st.session_state.dataset = "B"
with cols[4]:
    if st.button("Hierarchical Clustering", width='stretch'):
        st.session_state.dataset = "C"

data_map = {
    "A": df_1,
    "B": df_2,
    "C": df_3
}

df = data_map[st.session_state.dataset]

viridis_colors = {
    'Phát triển': '#f3722c',
    'Đang phát triển': '#f9c74f',
    'Kém phát triển': '#f94144'
}

if st.session_state.dataset == "A":
    st.markdown(
        """
        <h2 style='text-align: center; color: #2a9d8f;'>
        Phân cụm sử dụng Gaussian Mixture Model (GMM)</h2>
        """, unsafe_allow_html=True
    )
elif st.session_state.dataset == "B":
    st.markdown(
        """
        <h2 style='text-align: center; color: #2a9d8f;'>
        Phân cụm sử dụng KMeans Clustering</h2>
        """, unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <h2 style='text-align: center; color: #2a9d8f;'>
        Phân cụm sử dụng Hierarchical Clustering</h2>
        """, unsafe_allow_html=True
    )

fig = px.choropleth(df,
                    locations="Country_code",
                    color="Cluster",
                    hover_name="Country",
                    color_continuous_scale="Viridis",
                    color_discrete_map=viridis_colors,
                    labels={'Cluster': 'Mức độ phát triển'},
                    )

fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))

cols = st.columns([1, 3, 1])
with cols[1]:
    st.plotly_chart(fig, width='stretch')
