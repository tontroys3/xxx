import streamlit as st
import hashlib
from datetime import datetime

# Page config
st.set_page_config(
    page_title="StreamFlow - Live Streaming Platform",
    page_icon="🎥",
    layout="wide"
)

# Session state initialization
if 'user' not in st.session_state:
    st.session_state.user = None
if 'users' not in st.session_state:
    st.session_state.users = [
        {
            'id': 1,
            'username': 'admin',
            'email': 'admin@streamflow.com',
            'password_hash': hashlib.sha256('admin123'.encode()).hexdigest()
        }
    ]
if 'videos' not in st.session_state:
    st.session_state.videos = []
if 'streams' not in st.session_state:
    st.session_state.streams = []

# Authentication
def authenticate_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    for user in st.session_state.users:
        if user['username'] == username and user['password_hash'] == password_hash:
            return {'id': user['id'], 'username': user['username'], 'email': user['email']}
    return None

def create_user(username, email, password):
    for user in st.session_state.users:
        if user['username'] == username or user['email'] == email:
            return False
    
    new_user = {
        'id': len(st.session_state.users) + 1,
        'username': username,
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest()
    }
    st.session_state.users.append(new_user)
    return True

# Main app
def main():
    if st.session_state.user is None:
        # Login page
        st.title("🎥 StreamFlow - Live Streaming Platform")
        st.markdown("### Selamat Datang di StreamFlow")
        st.info("Platform demo untuk live streaming ke berbagai platform.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            tab1, tab2 = st.tabs(["Login", "Register"])
            
            with tab1:
                with st.form("login_form"):
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    login_button = st.form_submit_button("Login")
                    
                    if login_button:
                        if username and password:
                            user = authenticate_user(username, password)
                            if user:
                                st.session_state.user = user
                                st.rerun()
                            else:
                                st.error("Username atau password salah")
                        else:
                            st.error("Silakan masukkan username dan password")
                
                st.success("Demo Login: admin / admin123")
            
            with tab2:
                with st.form("register_form"):
                    new_username = st.text_input("Username Baru")
                    new_email = st.text_input("Email")
                    new_password = st.text_input("Password Baru", type="password")
                    register_button = st.form_submit_button("Daftar")
                    
                    if register_button:
                        if new_username and new_email and new_password:
                            if len(new_password) >= 8:
                                if create_user(new_username, new_email, new_password):
                                    st.success("Akun berhasil dibuat! Silakan login.")
                                else:
                                    st.error("Username atau email sudah digunakan")
                            else:
                                st.error("Password minimal 8 karakter")
                        else:
                            st.error("Silakan isi semua field")
    
    else:
        # Main dashboard
        st.title("🎥 StreamFlow Dashboard")
        st.markdown(f"### Selamat Datang, {st.session_state.user['username']}!")
        
        # Sidebar
        with st.sidebar:
            st.markdown(f"#### {st.session_state.user['username']}")
            st.markdown("---")
            
            page = st.selectbox("Navigasi", [
                "Dashboard", "Galeri Video", "Live Streaming", "Pengaturan"
            ])
            
            st.markdown("---")
            if st.button("Logout"):
                st.session_state.user = None
                st.rerun()
        
        # Main content
        if page == "Dashboard":
            col1, col2, col3 = st.columns(3)
            
            with col1:
                video_count = len([v for v in st.session_state.videos if v['user_id'] == st.session_state.user['id']])
                st.metric("Total Video", video_count)
            
            with col2:
                active_streams = len([s for s in st.session_state.streams if s['user_id'] == st.session_state.user['id'] and s.get('status') == 'active'])
                st.metric("Stream Aktif", active_streams)
            
            with col3:
                total_streams = len([s for s in st.session_state.streams if s['user_id'] == st.session_state.user['id']])
                st.metric("Total Stream", total_streams)
            
            st.markdown("---")
            st.subheader("Aksi Cepat")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Upload Video", use_container_width=True):
                    st.info("Navigasi ke Galeri Video untuk upload")
            
            with col2:
                if st.button("Buat Stream", use_container_width=True):
                    st.info("Navigasi ke Live Streaming untuk buat stream")
        
        elif page == "Galeri Video":
            st.subheader("Upload Video")
            uploaded_file = st.file_uploader("Pilih file video", type=['mp4', 'mov', 'avi', 'mkv'])
            
            if uploaded_file is not None:
                st.success(f"File {uploaded_file.name} siap diupload")
                
                if st.button("Simpan Video"):
                    new_video = {
                        'id': len(st.session_state.videos) + 1,
                        'user_id': st.session_state.user['id'],
                        'filename': uploaded_file.name,
                        'size': getattr(uploaded_file, 'size', 0),
                        'created_at': datetime.now().isoformat()
                    }
                    st.session_state.videos.append(new_video)
                    st.success("Video berhasil disimpan!")
                    st.rerun()
            
            st.markdown("---")
            st.subheader("Video Anda")
            
            user_videos = [v for v in st.session_state.videos if v['user_id'] == st.session_state.user['id']]
            
            if user_videos:
                for video in user_videos:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{video['filename']}** - {video['size']} bytes")
                    with col2:
                        if st.button(f"Hapus", key=f"del_{video['id']}"):
                            st.session_state.videos = [v for v in st.session_state.videos if v['id'] != video['id']]
                            st.rerun()
            else:
                st.info("Belum ada video")
        
        elif page == "Live Streaming":
            st.subheader("Buat Stream Baru")
            
            with st.form("stream_form"):
                title = st.text_input("Judul Stream")
                platform = st.selectbox("Platform", ["YouTube", "Facebook", "Twitch", "TikTok", "Instagram"])
                stream_key = st.text_input("Stream Key", type="password")
                
                if st.form_submit_button("Buat Stream"):
                    if title and platform and stream_key:
                        new_stream = {
                            'id': len(st.session_state.streams) + 1,
                            'user_id': st.session_state.user['id'],
                            'title': title,
                            'platform': platform,
                            'stream_key': stream_key,
                            'status': 'pending',
                            'created_at': datetime.now().isoformat()
                        }
                        st.session_state.streams.append(new_stream)
                        st.success("Stream berhasil dibuat!")
                        st.rerun()
                    else:
                        st.error("Silakan isi semua field")
            
            st.markdown("---")
            st.subheader("Stream Anda")
            
            user_streams = [s for s in st.session_state.streams if s['user_id'] == st.session_state.user['id']]
            
            if user_streams:
                for stream in user_streams:
                    with st.expander(f"{stream['title']} - {stream['platform']}"):
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            if st.button(f"Mulai", key=f"start_{stream['id']}"):
                                for i, s in enumerate(st.session_state.streams):
                                    if s['id'] == stream['id']:
                                        st.session_state.streams[i]['status'] = 'active'
                                st.success("Stream dimulai!")
                                st.rerun()
                        
                        with col2:
                            if st.button(f"Berhenti", key=f"stop_{stream['id']}"):
                                for i, s in enumerate(st.session_state.streams):
                                    if s['id'] == stream['id']:
                                        st.session_state.streams[i]['status'] = 'stopped'
                                st.success("Stream dihentikan!")
                                st.rerun()
                        
                        with col3:
                            if st.button(f"Hapus", key=f"del_stream_{stream['id']}"):
                                st.session_state.streams = [s for s in st.session_state.streams if s['id'] != stream['id']]
                                st.success("Stream dihapus!")
                                st.rerun()
            else:
                st.info("Belum ada stream")
        
        elif page == "Pengaturan":
            st.subheader("Informasi Akun")
            st.text_input("Username", value=st.session_state.user['username'], disabled=True)
            st.text_input("Email", value=st.session_state.user['email'], disabled=True)
            
            st.markdown("---")
            st.subheader("Tentang StreamFlow")
            st.markdown("""
            **StreamFlow v2.0** - Platform Live Streaming Multi-Platform
            
            Fitur:
            - Upload dan kelola video
            - Streaming ke berbagai platform
            - Dashboard monitoring
            - Pengaturan akun
            
            Dibuat dengan Streamlit
            """)

if __name__ == "__main__":
    main()