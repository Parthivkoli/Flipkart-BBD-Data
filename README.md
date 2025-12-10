# FLIPKART'S IT PREPAREDNESS FOR BIG BILLION DAYS (BBD)

<div align="center">
  <img src="https://mu.ac.in/wp-content/uploads/2020/07/MU-Logo.png" alt="University of Mumbai Logo" width="150" height="150">
  <img src="https://static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/fk-logo_f64bb3.png" alt="Flipkart Logo" width="150" height="150">
</div>

## Project Overview

This project analyzes Flipkart's IT infrastructure preparedness for Big Billion Days (BBD), focusing on monitoring, scalability, and reliability aspects. The analysis includes data visualization through diagrams and tables generated using Python scripts.

## University Details

**UNIVERSITY OF MUMBAI**  
**MUMBAI INSTITUTE OF MANAGEMENT & RESEARCH**  
Wadala (East), Mumbai- 400 037

**SUBMITTED IN PARTIAL FULFILMENT OF MASTERS IN MANAGEMENT STUDIES-SEMESTER III**  
**SPECIALIZATION: SYSTEMS(IT)**

## Submitted By

**NAME: PARTHIV**

## Project Structure

- `data.py`: Script for data processing and preparation
- `generate_all.py`: Main script to generate diagrams and tables
- `monitoring.mmd`: Mermaid diagram illustrating the monitoring architecture
- `requirements.txt`: Python dependencies
- `output/`: Generated outputs including HTML figures and tables
- `env/`: Virtual environment (not included in repo)

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```
   python generate_all.py
   ```

3. View the generated diagrams and tables in the `output/` directory.

## Monitoring Diagram

The `monitoring.mmd` file contains a Mermaid diagram showing Flipkart's monitoring setup, including Kubernetes clusters, Prometheus federation, Grafana dashboards, chaos testing, and Jaeger tracing.

## Technologies Used

- Python
- Matplotlib (for visualizations)
- Mermaid (for diagrams)
- Jupyter/Pandas (assumed for data handling)