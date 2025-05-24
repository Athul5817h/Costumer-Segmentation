# Customer Segmentation Flask Application

This repository contains a Flask-based web application that predicts customer segmentation using a machine learning model. The application collects customer data via a web form, stores it in a MongoDB database, and provides insights into customer segments. The app is deployed on [Render](https://render.com) for easy access.

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
  - [Local Setup](#local-setup)
  - [Deployment on Render](#deployment-on-render)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

1. **Predict Customer Segmentation**: Classifies customers into distinct groups based on their characteristics and behavior.
2. **Database Integration**: Stores user inputs in a MongoDB database for analysis and retrieval.
3. **Web Interface**: Offers an intuitive web-based interface for users to input data and view predictions.
4. **ML Integration**: Uses a pre-trained machine learning model (`customer_segmentation_model.pkl`).
5. **Deployed on Render**: Accessible from any browser without needing local setup.

---

## Screenshots

### Input Form
![Alt text](https://github.com/Athul5817h/Costumer-Segmentation/blob/master/Front%20page.png)

### Prediction Result
![Prediction Result](https://github.com/Athul5817h/Costumer-Segmentation/blob/master/Result%20page.png)

---

## Technologies Used

- **Python**: Flask for backend development.
- **HTML & CSS**: For designing the web interface.
- **MongoDB**: For data storage.
- **scikit-learn**: For the machine learning model.
- **Render**: For deployment.

---

## Installation and Setup

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/customer-segmentation.git
   cd customer-segmentation
