# Healthcare Analytics & Decision Support Dashboard  
[![home.png](https://i.postimg.cc/qqwXCzQ5/home.png)](https://postimg.cc/9w4q6X6d) 
## Introduction  
Healthcare institutions generate large volumes of data across patient care, operations, and finances. Often, this data is siloed and underutilized, limiting its value in decision-making.  

The **Healthcare Analytics & Decision Support Dashboard** integrates patient, clinical, hospital, and financial data into a unified analytics platform. Using **SQL** for backend queries and **Power BI** for visualization, the dashboard empowers administrators, doctors, and finance teams to make **data-driven decisions** with real-time insights.  

---

## Key Features  
- **Patient Analytics** → Monitor admissions, discharges, demographics, and treatment insights.  
- **Doctor Analytics** → Track physician performance, appointments, and commission-based earnings.  
- **Hospital Operations** → View resource allocation, bed occupancy, staff schedules, and surgeries.  
- **Financial Insights** → Analyze revenue, expenses, payments, and supplier contributions.  
- **Interactive Dashboards** → Role-based visualizations for patients, doctors, admins, and finance teams.  

---

## Tech Stack  
- **Database**: MySQL Server (data storage & queries)  
- **Visualization**: Power BI  
- **Languages/Tools**: SQL, DAX, Excel  
- **Repository Organization**:  
  - `/data` → Datasets (CSV files)  
  - `/scripts` → Sql Queries  
  - `/dashboard` → Power BI `.pbix` file
  - `/images` → dashboard screenshots  
  - `/docs` → Executive Summary, BRD & FRD

---

## Dashboards  

Below are the dashboards included in this project. Each section includes a screenshot and a short description of its purpose and key insights.  

### 1. Home Dashboard  
[![home.png](https://i.postimg.cc/qqwXCzQ5/home.png)](https://postimg.cc/9w4q6X6d) 
**Purpose:** Landing page for navigation.   
- Navigation buttons for each section: **Overview, Patient, Doctor, Hospital, Finance**.  

---

### 2. Overview Dashboard  
[![overview.png](https://i.postimg.cc/Wp71JM61/overview.png)](https://postimg.cc/xqc2wN4w)
**Purpose:** High-level summary of hospital performance.  
- KPIs: Patients, Doctors, Staff, Revenue.  
- Trend graph of activity over time.  
- Bed status & medical stock availability.  
- Patient feedback, medicine purchase patterns, charges by category.  
- Upcoming appointments and recent admissions/discharges.  

---

### 3. Patient Dashboard  
[![patient.png](https://i.postimg.cc/QdJ98R46/patient.png)](https://postimg.cc/ZW0KjDh3) 
**Purpose:** Detailed view of an individual patient.  
- Profile: Patient details, attending doctor, diagnosis, feedback rating.  
- Stay Summary: Admission/discharge dates, total medicines bought, amount paid.  
- Charges breakdown by category (surgery, room, tests, etc.).  
- Medicines bought with quantities + calendar of purchase dates.  

---

### 4. Doctor Dashboard  
[![doctor.png](https://i.postimg.cc/KYcNx7NB/doctor.png)](https://postimg.cc/YvVgxWTC)  
**Purpose:** Track doctor performance, appointments, and earnings.  
- Profile: Name, specialty, salary, experience, ratings.  
- Financial Overview: Patient-paid amounts, commissions, earnings.  
- Interactive Commission Calculator.  
- Appointments list + detailed patient table (services, bills, ratings).  

---

### 5. Hospital Dashboard  
[![hospital.png](https://i.postimg.cc/13VSM66F/hospital.png)](https://postimg.cc/v4yCZ408) 
**Purpose:** Monitor hospital-wide operations and resources.  
- Patient demographics by age group.  
- Test status & surgeries list.  
- Bed occupancy breakdown (General, Private, ICU).  
- Doctors appointment schedules.  

---

### 6. Finance Dashboard  
[![finance.png](https://i.postimg.cc/c48kbc9f/finance.png)](https://postimg.cc/SJkGXcpK) 
**Purpose:** Consolidated financial health of the hospital.  
- KPIs: Total patients, paid amounts, salaries, commissions, profit.  
- Revenue trends by payment method (cash, credit card, insurance).  
- Charges by category (surgery, room, tests, medicine, etc.).  
- Medicine inventory & supplier contributions.  

---

## Documentation  
- [Business Requirements Document (BRD)](docs/BRD.pdf)  
- [Functional Requirements Document (FRD)](docs/FRD.pdf)  
- [Executive Summary](docs/Executive_Summary.pdf)

---

## Results & Impact  
- Improved **decision-making speed** with centralized dashboards.  
- Enabled **real-time hospital monitoring** across operations, patients, and finance.  
- Delivered **predictive insights** for patient load and resource allocation.  
- Increased transparency in **doctor performance and financial reporting**.  

---

## Future Enhancements  
- AI/ML integration for patient risk prediction.  
- Automated ETL pipelines for real-time data refresh.  
- Expansion to include **public health & insurance datasets**.  
- Web-based deployment beyond Power BI desktop.  

---

> This project demonstrates the integration of hospital data into interactive dashboards for improved operational efficiency and informed decision-making.
