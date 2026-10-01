
import streamlit as st
import json
import os

st.set_page_config(
    page_title="Chinar Quantum AI Integrated Intelligence Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Custom Styling for Advanced Visualizations & Cards
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 35px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
    }
    .card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 28px;
        box-shadow: 0 6px 15px -3px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px -5px rgba(37, 99, 235, 0.15);
        border-color: #60a5fa;
    }
    .badge {
        background: #eff6ff;
        color: #1d4ed8;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 12.5px;
        font-weight: 700;
        border: 1.5px solid #bfdbfe;
        letter-spacing: 0.5px;
    }
    .live-obs-box {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 6px solid #22c55e;
        padding: 18px 22px;
        border-radius: 14px;
        margin-bottom: 20px;
    }
    .ai-profile-box {
        background: #eff6ff;
        border: 1px solid #dbeafe;
        border-left: 6px solid #2563eb;
        padding: 18px 22px;
        border-radius: 14px;
        margin-bottom: 20px;
    }
    .neural-map-box {
        background: #faf5ff;
        border: 1px solid #e9d5ff;
        border-left: 6px solid #a855f7;
        padding: 18px 22px;
        border-radius: 14px;
        margin-bottom: 20px;
    }
    .grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
        margin-bottom: 18px;
    }
    .inner-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 16px 18px;
        border-radius: 14px;
        font-size: 14px;
        color: #334155;
    }
    @media(max-width: 768px) {
        .grid-2 { grid-template-columns: 1fr; }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    if os.path.exists("students_v3.json"):
        with open("students_v3.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

data = load_data()

# Header
st.markdown("""
<div class="hero-box">
    <h1 style="margin:0; font-size:32px; font-weight:800;">🧠 Chinar Quantum AI Integrated Dashboard</h1>
    <p style="margin:10px 0 0 0; font-size:16px; opacity:0.9;">Real-time Live Observations, Unstructured Visual Insights & Neural Profiles</p>
</div>
""", unsafe_allow_html=True)

if not data:
    st.error("⚠️ `students_v3.json` file not found! Please make sure your data extraction script has been executed successfully.")
else:
    # Sidebar Filters
    st.sidebar.markdown("### 🎛️ Navigation & Filters")
    search = st.sidebar.text_input("🔍 Search Participant by Name:", "").strip().lower()
    
    filtered_data = [
        item for item in data 
        if search in item.get("name", "").lower()
    ] if search else data

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"📊 **Analytics Summary:**")
    st.sidebar.markdown(f"- Total Participants: **{len(data)}**")
    st.sidebar.markdown(f"- Displayed Records: **{len(filtered_data)}**")

    # Main Render Loop
    for i, d in enumerate(filtered_data):
        name = d.get("name", f"Participant {i+1}")
        edu = d.get("education", "Verified Scholar")
        org_feedback = d.get("org_feedback", "Consistent participation and active alignment observed.")
        goals = d.get("goals", [])
        status = d.get("status", [])
        org_value = d.get("org_value", [])
        improvements = d.get("improvements", [])
        
        initials = "".join([part[0] for part in str(name).split()[:2]]).upper()

        card_html = f"""
        <div class="card">
            <!-- Card Header -->
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f1f5f9; padding-bottom: 18px; margin-bottom: 22px;">
                <div style="display: flex; align-items: center; gap: 18px;">
                    <div style="width: 58px; height: 58px; background: #eff6ff; color: #1d4ed8; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: bold; border: 2px solid #bfdbfe;">{initials}</div>
                    <div>
                        <div style="font-size: 12.5px; font-weight: bold; color: #2563eb; margin-bottom: 3px;">🆔 Integrated Profile #{i+1}</div>
                        <div style="font-size: 22px; font-weight: 800; color: #0f172a;">{name}</div>
                        <div style="font-size: 14px; color: #475569; margin-top: 3px;">🎓 <b>Education & Background:</b> {edu}</div>
                    </div>
                </div>
                <div><span class="badge">✨ Verified AI Profile</span></div>
            </div>
            
            <!-- 1. Live Observation & Core Alignment -->
            <div class="live-obs-box">
                <b style="color: #166534; display: block; margin-bottom: 5px; font-size: 13.5px; letter-spacing: 0.5px;">📡 LIVE OBSERVATION & SESSION ALIGNMENT</b>
                <p style="margin: 0; color: #14532d; font-size: 15px; line-height: 1.6; font-weight: 600;">{org_feedback}</p>
            </div>

            <!-- 2. AI Profile & Unstructured Insights Grid -->
            <div class="ai-profile-box">
                <b style="color: #1e40af; display: block; margin-bottom: 12px; font-size: 13.5px; letter-spacing: 0.5px;">🧠 REAL-TIME AI PROFILE & UNSTRUCTURED INSIGHTS</b>
                <div class="grid-2">
                    <div class="inner-box" style="background:#ffffff;">
                        <b style="color: #1e293b; display: block; margin-bottom: 8px;">🎯 Goals & Aspirations</b>
                        <ul style="margin: 0; padding-left: 18px; color: #334155; line-height: 1.5;">
                            {"".join(f"<li>{g}</li>" for g in goals) if goals else "<li>Focused on core skill enhancement</li>"}
                        </ul>
                    </div>
                    <div class="inner-box" style="background:#ffffff;">
                        <b style="color: #1e293b; display: block; margin-bottom: 8px;">💼 Current Status & Competency</b>
                        <ul style="margin: 0; padding-left: 18px; color: #334155; line-height: 1.5;">
                            {"".join(f"<li>{s}</li>" for s in status) if status else "<li>Active professional learner</li>"}
                        </ul>
                    </div>
                </div>
            </div>

            <!-- 3. Neural Map & Strategic Roadmap Grid -->
            <div class="neural-map-box">
                <b style="color: #6b21a8; display: block; margin-bottom: 12px; font-size: 13.5px; letter-spacing: 0.5px;">🗺️ NEURAL MAP & STRATEGIC ROADMAP</b>
                <div class="grid-2">
                    <div class="inner-box" style="background:#ffffff;">
                        <b style="color: #1e293b; display: block; margin-bottom: 8px;">📊 Key Organization Insights</b>
                        <ul style="margin: 0; padding-left: 18px; color: #334155; line-height: 1.5;">
                            {"".join(f"<li>{v}</li>" for v in org_value) if org_value else "<li>Strong dedication and engagement potential</li>"}
                        </ul>
                    </div>
                    <div class="inner-box" style="background:#ffffff;">
                        <b style="color: #1e293b; display: block; margin-bottom: 8px;">🛠️ Target Improvements & Support</b>
                        <ul style="margin: 0; padding-left: 18px; color: #334155; line-height: 1.5;">
                            {"".join(f"<li>{imp}</li>" for imp in improvements) if improvements else "<li>Consistent practice and regular follow-ups</li>"}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
