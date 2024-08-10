import os

# Define the structure with divisions, districts, and organizations
structure = {
    "Dhaka": ["Dhaka", "Faridpur", "Gazipur", "Gopalganj", "Kishoreganj", "Madaripur", "Manikganj", "Munshiganj", "Narayanganj", "Narsingdi", "Rajbari", "Shariatpur", "Tangail"],
    "Chattogram": ["Bandarban", "Brahmanbaria", "Chandpur", "Chattogram", "Cumilla", "Cox's Bazar", "Feni", "Khagrachari", "Lakshmipur", "Noakhali", "Rangamati"],
    "Khulna": ["Bagerhat", "Chuadanga", "Jashore", "Jhenaidah", "Khulna", "Kushtia", "Magura", "Meherpur", "Narail", "Satkhira"],
    "Rajshahi": ["Bogura", "Joypurhat", "Naogaon", "Natore", "Chapai Nawabganj", "Pabna", "Rajshahi", "Sirajganj"],
    "Barishal": ["Barguna", "Barishal", "Bhola", "Jhalokathi", "Patuakhali", "Pirojpur"],
    "Sylhet": ["Habiganj", "Moulvibazar", "Sunamganj", "Sylhet"],
    "Rangpur": ["Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Rangpur", "Thakurgaon"],
    "Mymensingh": ["Jamalpur", "Mymensingh", "Netrokona", "Sherpur"]
}

organizations = [
    "Bangladesh Chhatra League",
    "Bangladesh Awami Jubo League",
    "Bangladesh Krishak League",
    "Bangladesh Jatiya Sramik League"
]

# Template content for .md files with counters
template_content = """\
# {organization} in {district}, {division}

## Members List

1. **Name:**
   - **Position:**
   - **Home Address:**
   - **Phone Number:**
   - **Activity Photos:** [Upload photos here or provide a link]
   - **Video Links:** [Upload videos here or provide a link]

2. **Name:**
   - **Position:**
   - **Home Address:**
   - **Phone Number:**
   - **Activity Photos:** [Upload photos here or provide a link]
   - **Video Links:** [Upload videos here or provide a link]

3. **Name:**
   - **Position:**
   - **Home Address:**
   - **Phone Number:**
   - **Activity Photos:** [Upload photos here or provide a link]
   - **Video Links:** [Upload videos here or provide a link]

...

(Continue adding new members below with an incremented counter)
"""

# Create the structure within the current directory (assumed to be Razakar24)
for division, districts in structure.items():
    for district in districts:
        for organization in organizations:
            # Create directory path
            dir_path = os.path.join(division, district, organization)
            os.makedirs(dir_path, exist_ok=True)

            # Create .md file inside the directory
            file_name = organization.replace(" ", "") + ".md"
            file_path = os.path.join(dir_path, file_name)

            # Write header and initial template content to the .md file
            with open(file_path, 'w') as f:
                f.write(template_content.format(organization=organization, district=district, division=division))
