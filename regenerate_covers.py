import os
import requests
import re

posts_dir = r"c:\Users\admin\GitHubProject\FC\content\posts"
article_folders = [f for f in os.listdir(posts_dir) if os.path.isdir(os.path.join(posts_dir, f))]

print(f"Found {len(article_folders)} article folders.")

def read_article_content(folder_path):
    md_file = os.path.join(folder_path, "index.md")
    if os.path.exists(md_file):
        with open(md_file, "r", encoding="utf-8") as f:
            return f.read()
    return None

def extract_title_and_description(content):
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    description_match = re.search(r'description:\s*"([^"]+)"', content)
    title = title_match.group(1) if title_match else ""
    description = description_match.group(1) if description_match else title
    return title, description

def generate_cover_image(prompt, output_path):
    try:
        encoded_prompt = requests.utils.quote(prompt)
        url = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={encoded_prompt}&image_size=square_hd"
        
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        
        with open(output_path, "wb") as f:
            f.write(response.content)
        
        print(f"Generated cover image: {output_path}")
        return True
    except Exception as e:
        print(f"Error generating cover for {output_path}: {e}")
        return False

def get_image_prompt(title, description, folder_name):
    base_prompts = {
        "ai-in-healthcare": "Artificial intelligence in healthcare, modern medical technology with neural networks and digital brain, futuristic hospital setting, doctor and robot working together, medical imaging, ethical balance between technology and humanity, professional, clean, blue tones",
        "ai-in-software-development": "AI in software development, futuristic coding environment, neural networks writing code, developers collaborating with AI assistants, code editors with AI suggestions, modern tech workspace, purple and blue colors",
        "art-creativity": "Art and creativity, vibrant colorful painting studio, abstract art, paintbrushes, canvas, artist palette, creative inspiration, rainbow colors, modern art gallery",
        "blockchain-digital-economy": "Blockchain and digital economy, futuristic financial technology, cryptocurrency, decentralized networks, digital transactions, blockchain blocks, secure data, blue and green tones",
        "city-nature-balance": "Balance between city and nature, futuristic eco-city, skyscrapers with vertical gardens, green spaces in urban areas, sustainable architecture, harmony between technology and nature",
        "climate-change-global-cooperation": "Climate change and global cooperation, world map with connected nations, environmental protection, renewable energy, wind turbines, solar panels, green earth, hands holding together, blue and green colors",
        "cultural-diversity": "Cultural diversity, people from different countries together, world flags, traditional clothing, global unity, colorful celebration, multicultural harmony",
        "cultural-diversity-globalization": "Cultural diversity and globalization, interconnected world, people from diverse backgrounds, traditional and modern fusion, global village, cultural exchange, vibrant colors",
        "digital-art-rising": "Digital art rising, futuristic digital canvas, digital painting tools, creative technology, glowing pixels, digital artist workspace, neon colors",
        "digital-minimalism": "Digital minimalism, clean simple workspace, minimal design, decluttered digital life, calm and peaceful, monochrome colors, modern simplicity",
        "digital-privacy": "Digital privacy and security, padlock on digital data, secure internet, cybersecurity, encrypted information, privacy protection, blue tones, professional",
        "digital-privacy-protection": "Digital privacy protection, shield protecting personal data, cybersecurity, encrypted communication, secure online browsing, privacy shield, blue and green",
        "eco-tech-sustainable-living": "Eco tech and sustainable living, renewable energy, smart home with green technology, solar panels, wind turbines, eco-friendly lifestyle, sustainable future",
        "education-future": "Future of education, modern classroom with technology, students learning with VR and AI, digital textbooks, futuristic learning environment, bright colors",
        "education-innovation": "Education innovation, creative learning, modern teaching methods, technology in classroom, innovative education tools, students and teachers collaborating",
        "entrepreneurship-innovation": "Entrepreneurship and innovation, startup office, creative brainstorming, business innovation, modern workspace, entrepreneurs working, dynamic and energetic",
        "future-transport-smart-city": "Future transport and smart city, autonomous vehicles, flying cars, smart city infrastructure, futuristic transportation, sustainable mobility, high-tech",
        "game-design-zelda": "Zelda game design, open world adventure, Hyrule landscape, Master Sword, mystical fantasy world, Link exploring, Nintendo style, epic adventure, green and blue tones",
        "healthy-eating": "Healthy eating, fresh fruits and vegetables, balanced diet, nutrition, colorful food, healthy lifestyle, organic produce, vibrant kitchen",
        "japan-travel-experience": "Japan travel experience, Tokyo skyline with Mount Fuji, traditional Japanese temple, cherry blossoms, sushi, cultural mix of modern and traditional, red and white colors",
        "learning-new-skills": "Learning new skills, online courses, skill development, knowledge growth, books and digital learning, education journey, growth mindset, warm colors",
        "mental-health-digital-stress": "Mental health and digital stress, mindfulness, meditation, digital detox, mental wellness, calm and peaceful, nature elements, blue and green tones",
        "metaverse-digital-identity": "Metaverse and digital identity, virtual reality, digital avatars, online world, futuristic technology, virtual space, neon colors, cyberpunk style",
        "mindfulness-practice": "Mindfulness practice, meditation, yoga, calm peaceful environment, nature, zen garden, mindfulness meditation, serenity, soft colors",
        "movie-review-interstellar": "Interstellar movie, space exploration, wormhole, black hole, astronauts, epic space journey, stars and galaxies, science fiction, cinematic",
        "my-blog-setup-guide": "Blog setup guide, modern workspace, laptop and coffee, content creation, writing and publishing, cozy office, warm tones",
        "remote-work-future": "Remote work future, digital nomad, working from anywhere, laptop in beautiful location, work-life balance, flexible work, modern technology",
        "simple-life-happiness": "Simple life and happiness, minimalist lifestyle, peaceful moments, nature, gratitude, contentment, slow living, warm and cozy",
        "space-exploration-future": "Future of space exploration, astronauts on Mars, space stations, rocket ships, galaxies and nebulae, cosmic adventure, futuristic space travel",
        "sustainable-urban-planning": "Sustainable urban planning, eco-friendly city, green buildings, public transport, walkable neighborhoods, sustainable architecture, green and blue",
        "tech-innovation-traditional-industry": "Technology innovation in traditional industry, modern tech meeting traditional craftsmanship, digital transformation, industry 4.0, innovation bridge"
    }
    
    if folder_name in base_prompts:
        return base_prompts[folder_name]
    
    return f"Blog post cover for: {title}. {description}. Professional, visually appealing, high quality, blog cover image."

for folder in article_folders:
    folder_path = os.path.join(posts_dir, folder)
    content = read_article_content(folder_path)
    
    if content:
        title, description = extract_title_and_description(content)
        print(f"\nProcessing: {folder}")
        print(f"Title: {title}")
        
        prompt = get_image_prompt(title, description, folder)
        output_path = os.path.join(folder_path, "cover.jpg")
        
        generate_cover_image(prompt, output_path)
    else:
        print(f"Warning: No index.md found in {folder}")

print("\nDone!")
