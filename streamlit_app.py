import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="PT. Jaring Rezeki Halal - IT Solutions",
    page_icon="🌐",
    initial_sidebar_state="collapsed",
    layout="wide"
)

# --- CUSTOM CSS FOR STYLING ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Using a multi-line string for CSS to avoid needing a separate file
local_css_def = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Lato:wght@400;700&display=swap');

/* General Styles */
body {
    font-family: 'Lato', sans-serif;
    color: #333333;
}
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif;
    color: #0A2540; /* Dark Blue */
}
h1 {
    font-size: 3.5rem;
    font-weight: 700;
}
h2 {
    font-size: 2.5rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 2.5rem;
}
h3 {
    font-size: 1.5rem;
    font-weight: 600;
}

/* Header/Hero Section */
.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    color: #0A2540;
    line-height: 1.2;
}
.hero-subtitle {
    font-size: 1.2rem;
    color: #555555;
    margin-bottom: 2rem;
}

/* Custom Button */
.custom-button {
    background-color: #00C1D4; /* Accent Teal */
    color: white;
    padding: 12px 28px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 50px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
    font-family: 'Poppins', sans-serif;
    border: none;
}
.custom-button:hover {
    background-color: #00A8B8;
    transform: translateY(-2px);
    color: white;
    text-decoration: none;
}

/* Service Cards */
.service-card {
    background-color: #f8f9fa;
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    height: 100%;
    transition: transform 0.3s, box-shadow 0.3s;
    border-left: 5px solid #00C1D4;
}
.service-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.service-icon {
    font-size: 3rem;
    color: #00C1D4;
    margin-bottom: 1rem;
}

/* Why Choose Us Section */
.feature-card {
    text-align: center;
    padding: 1.5rem;
}
.feature-icon {
    font-size: 2.5rem;
    color: #0A2540;
    margin-bottom: 1rem;
}
.feature-title {
    font-weight: 700;
    margin-bottom: 0.5rem;
}

/* About Section */
.about-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
}
.about-image-container img {
    max-width: 100%;
    border-radius: 10px;
}

/* Contact Section */
#contact {
    padding: 3rem 0;
    background-color: #f8f9fa;
    border-radius: 10px;
}
.contact-info {
    font-size: 1.1rem;
}
.contact-info p {
    margin-bottom: 0.5rem;
}
.contact-info i {
    color: #00C1D4;
    margin-right: 10px;
    width: 20px;
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
    border-top: 1px solid #e0e0e0;
}
.social-icons a {
    color: #0A2540;
    font-size: 1.5rem;
    margin: 0 10px;
    transition: color 0.3s;
}
.social-icons a:hover {
    color: #00C1D4;
}

/* Streamlit Element Hiding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.st-emotion-cache-1y4p8pa {padding-top: 0;}

</style>
"""
st.markdown(local_css_def, unsafe_allow_html=True)


# --- FONT AWESOME FOR ICONS ---
font_awesome = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""
st.markdown(font_awesome, unsafe_allow_html=True)


# --- HERO SECTION ---
with st.container():
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<h1 class="hero-title">Empowering Your Business with Premier IT Solutions</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">PT. Jaring Rezeki Halal delivers innovative, reliable, and secure technology to drive your success in the digital age.</p>', unsafe_allow_html=True)
        st.markdown('<a href="#contact" class="custom-button">Get In Touch</a>', unsafe_allow_html=True)
    with col2:
        # Replace with a real image of your team or office
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80", caption="Innovative Technology Solutions")

# --- SERVICES SECTION ---
st.markdown("---")
st.markdown('<h2>Our Services</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <i class="fas fa-laptop-code service-icon"></i>
        <h3>Web Development</h3>
        <p>Creating stunning, responsive, and high-performance websites tailored to your brand and business goals.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <i class="fas fa-mobile-alt service-icon"></i>
        <h3>Mobile App Solutions</h3>
        <p>Building intuitive and powerful native and cross-platform mobile applications for iOS and Android.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <i class="fas fa-cloud service-icon"></i>
        <h3>Cloud & DevOps</h3>
        <p>Streamlining your operations with scalable cloud infrastructure and automated deployment pipelines.</p>
    </div>
    """, unsafe_allow_html=True)

# --- WHY CHOOSE US SECTION ---
st.markdown("---")
st.markdown('<h2>Why Choose PT. Jaring Rezeki Halal?</h2>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <i class="fas fa-users feature-icon"></i>
        <div class="feature-title">Expert Team</div>
        <p>Our certified professionals bring years of experience to every project.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <i class="fas fa-rocket feature-icon"></i>
        <div class="feature-title">On-Time Delivery</div>
        <p>We are committed to delivering projects on schedule, without compromising quality.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <i class="fas fa-shield-alt feature-icon"></i>
        <div class="feature-title">Secure Solutions</div>
        <p>Security is at the forefront of our design and development process.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <i class="fas fa-headset feature-icon"></i>
        <div class="feature-title">24/7 Support</div>
        <p>We offer round-the-clock support to ensure your systems run smoothly.</p>
    </div>
    """, unsafe_allow_html=True)

# --- ABOUT US SECTION ---
st.markdown("---")
st.markdown('<h2>About Us</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1521791136064-7986c2920216?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80", caption="Our Vision")
with col2:
    st.markdown("""
    <h3>Building a Digital Future, Together.</h3>
    <p>At PT. Jaring Rezeki Halal, we are more than just an IT provider; we are your strategic partner in technology. Our mission is to bridge the gap between complex technology and business growth, providing solutions that are not only effective but also align with our core values of integrity and trust.</p>
    <p>We believe in creating "Halal" digital pathways—solutions that are transparent, ethical, and bring "Rezeki" (prosperity) to our clients and community. Our "Jaring" (network) is built on expertise, innovation, and a relentless commitment to your success.</p>
    """, unsafe_allow_html=True)


# --- CONTACT SECTION ---
st.markdown("---")
st.markdown('<div id="contact"></div>', unsafe_allow_html=True) # Anchor for link
st.markdown('<h2>Contact Us</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="contact-info">
        <h3>Let's Discuss Your Project</h3>
        <p>We're here to answer any questions and help you find the right solutions for your business needs.</p>
        <p><i class="fas fa-envelope"></i> <strong>Email:</strong> jaringrezekihalal@gmail.com</p>
        <p><i class="fas fa-phone"></i> <strong>Phone:</strong> +62 812-3456-7890</p>
        <p><i class="fas fa-map-marker-alt"></i> <strong>Address:</strong> Jakarta, Indonesia</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.write("Send us a message directly:")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        if submitted:
            st.success("Thank you for your message! We will get back to you soon.")
            # In a real application, you would send this data to an email or a database.

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>&copy; 2024 PT. Jaring Rezeki Halal. All Rights Reserved.</p>
    <div class="social-icons">
        <a href="#"><i class="fab fa-linkedin"></i></a>
        <a href="#"><i class="fab fa-facebook"></i></a>
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-instagram"></i></a>
    </div>
</div>
""", unsafe_allow_html=True)
