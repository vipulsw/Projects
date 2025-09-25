import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mulitple Disease Prediction",layout="wide")
working_dir = os.path.dirname(os.path.abspath(__file__))

kidney_disease_model = pickle.load(open(f'{working_dir}/Models/kidney_disease_final.pkl','rb'))
liver_disease_model = pickle.load(open(f'{working_dir}/Models/liver.pkl','rb'))
parkinson_disease_model = pickle.load(open(f'{working_dir}/Models/Parkinson_disease.pkl','rb'))
breast_cancer_model = pickle.load(open(f'{working_dir}/Models/breast_cancer-2.pkl','rb'))


with st.sidebar:
        selected = option_menu(menu_title = "Mulitple Disease Prediction", 
                options = ['Kidney Disease Prediction',
                 'Liver Disease Prediction',
                 'Parkinson Disease Prediction',
                 'Breast Cancer Prediction'],
                 default_index=0,
                 orientation="horizontal")

if selected == 'Kidney Disease Prediction':
    
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin')

    with col5:
        sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')

    with col2:
        pus_cell = st.text_input('Pus Cell')

    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')

    with col4:
        bacteria = st.text_input('Bacteria')

    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')

    with col1:
        blood_urea = st.text_input('Blood Urea')

    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')

    with col3:
        sodium = st.text_input('Sodium')

    with col4:
        potassium = st.text_input('Potassium')

    with col5:
        haemoglobin = st.text_input('Haemoglobin')

    with col1:
        packed_cell_volume = st.text_input('Packet Cell Volume')

    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
        hypertension = st.text_input('Hypertension')

    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
        appetite = st.text_input('Appetitte')

    with col3:
        peda_edema = st.text_input('Peda Edema')
    with col4:
        aanemia = st.text_input('Aanemia')

    # code for Prediction
    kindey_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Kidney's Test Result"):

        user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
       red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
       blood_glucose_random, blood_urea, serum_creatinine, sodium,
       potassium, haemoglobin, packed_cell_volume,
       white_blood_cell_count, red_blood_cell_count, hypertension,
       diabetes_mellitus, coronary_artery_disease, appetite,
       peda_edema, aanemia]

        user_input = [float(x) for x in user_input]

        prediction = kidney_disease_model.predict([user_input])

        if prediction[0] == 1:
            kindey_diagnosis = "The person has Kidney's disease"
        else:
            kindey_diagnosis = "The person does not have Kidney's disease"
    st.success(kindey_diagnosis)

if selected == 'Liver Disease Prediction':
    st.title("Liver Disease Prediction Using Machine Learning")
    col1, col2, col3  = st.columns(3)

    with col1:
        age = st.text_input("Your Age")
    with col2:
        gender = st.text_input("Gender")
    with col3:
        Total_Bilirubin = st.text_input("Total Bilirubin level")
    with col1:
        Direct_Bilirubin = st.text_input("Direct Bilirubin Measured")
    with col2:
        Alkaline_Phosphotase = st.text_input("Alkaline Phosphataase level")
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase level')
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase level')
    with col2:
        Total_Protiens = st.text_input("Total protein level")
    with col3:
        Albumin = st.text_input("Albumin level")
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input("Albumin and Globulin ratio value")

    # code for Prediction
    liver_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Liver Test Result"):

        user_input = [age, gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                      Alamine_Aminotransferase, Aspartate_Aminotransferase,Total_Protiens,
                      Albumin, Albumin_and_Globulin_Ratio]

        user_input = [float(x) for x in user_input]

        prediction = liver_disease_model.predict([user_input])

        if prediction[0] == 1:
            liver_diagnosis = "Have Liver disease"
        else:
            liver_diagnosis = "The person does not have Liver disease"
    st.success(liver_diagnosis)


if selected == 'Parkinson Disease Prediction':
    st.title("Parkinson's Disease Prediction Using Machine Learning")
    col1, col2, col3  = st.columns(3)

    with col1:
        MDVPFo = st.text_input("Average vocal fundamental frequency in Hertz")
    with col2:
        MDVPFhi = st.text_input("Maximum vocal fundamental frequency in Hertz")
    with col3:
        MDVPFlo = st.text_input("Minimum vocal fundamental frequency in Hertz")
    with col1:
        MDVPJitter = st.text_input("MDVP jitter in percentage")
    with col2:
        MDVPJitterAbs = st.text_input("MDVP absolute jitter in ms")
    with col3:
        MDVPRAP = st.text_input("MDVP relative amplitude perturbation")
    with col1:
        MDVPPPQ = st.text_input("MDVP five-point period perturbation quotient")
    with col2:
        JitterDDP = st.text_input("Average absolute difference of differences between jitter cycles")
    with col3:
        MDVPShimmer = st.text_input("MDVP local shimmer")
    with col1:
        MDVPShimmer = st.text_input("MDVP local shimmer in dB")
    with col2:
        ShimmerAPQ3 = st.text_input("Three-point amplitude perturbation quotient")
    with col3:
        ShimmerAPQ5 = st.text_input("Five-point amplitude perturbation quotient")
    with col1:
        MDVPAPQ = st.text_input("MDVP 11-point amplitude perturbation quotient")
    with col2:
        ShimmerDDA = st.text_input("Average absolute differences between the amplitudes of consecutive periods")
    with col3:
        NHR = st.text_input("Noise-to-harmonics ratio")
    with col1:
        HNR = st.text_input("Harmonics-to-noise ratio")
    with col2:
        RPDE = st.text_input("Recurrence period density entropy measure")
    with col3:
        DFA = st.text_input("Signal fractal scaling exponent of detrended fluctuation analysis")
    with col1:
        spread1 = st.text_input("Two nonlinear measures of fundamental")
    with col2:
        spread2 = st.text_input("Frequency variation")
    with col3:
        D2 = st.text_input("Correlation dimension")
    with col1:
        PPE = st.text_input("Pitch period entropy")

     # code for Prediction
    Parkinson_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson Test Result"):

        user_input = ['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP',
                      'MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5',
                      'MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE']

        user_input = [float(x) for x in user_input]

        prediction = parkinson_disease_model.predict([user_input])

        if prediction[0] == 1:
            Parkinson_diagnosis_diagnosis = "Have Parkinson disease"
        else:
            Parkinson_diagnosis_diagnosis = "The person does not have Parkinson disease"
    st.success(Parkinson_diagnosis)

if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction Using Machine Learning")
    col1, col2, col3, col4  = st.columns(4)

    with col1:
        radius_mean = st.text_input("Radius mean")
    with col2:
        texture_mean = st.text_input("Texture mean")
    with col3:
        perimeter_mean = st.text_input("The perimeter mean")
    with col4:
        area_mean = st.text_input("Area mean")
    with col1:
        smoothness_mean = st.text_input("Smoothness mean")
    with col2:
        compactness_mean = st.text_input("Compactness mean")
    with col3:
        concavity_mean = st.text_input("Concavity mean")
    with col4:
        concave_points_mean = st.text_input("Concave point mean")
    with col1:
        symmetry_mean = st.text_input("Symmetry mean")
    with col2:
        fractal_dimension_mean = st.text_input("Fractal dimension mean")
    with col3:
        radius_se = st.text_input("Radius_se")
    with col4:
        texture_se = st.text_input("Texture_se")
    with col1:
        perimeter_se = st.text_input("Perimeter_se")
    with col2:
        area_se = st.text_input("Area_se")
    with col3:
        smoothness_se = st.text_input("smoothness_se")
    with col4:
        compactness_se = st.text_input("Compactnes_se")
    with col1:
        concavity_se = st.text_input("Concavity_se")
    with col2:
        concave_points_se = st.text_input("Concave_points_se")
    with col3:
        symmetry_se = st.text_input("Summary_se")
    with col4:
        fractal_dimension_se = st.text_input("Fractal dimension_se")
    with col1:
        radius_worst = st.text_input("Radius worst")
    with col2:
        texture_worst = st.text_input("Texture worst")
    with col3:
        perimeter_worst = st.text_input("The perimeter worst")
    with col4:
        area_worst = st.text_input("Area worst")
    with col1:
        smoothness_worst = st.text_input("Smoothness worst")
    with col2:
        compactness_worst = st.text_input("Compactness worst")
    with col3:
        concavity_worst = st.text_input("Concavity worst")
    with col4:
        concave_points_worst = st.text_input("Concave_points worst")
    with col1:
        symmetry_worst = st.text_input("Summary worst")
    with col2:
        fractal_dimension_worst = st.text_input("Fractal dimension worst")

     # code for Prediction
    Breast_cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Breast Cancer Diagnosis Result"):

        user_input = ['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean',
                      'concavity_mean','concave_points_mean','symmetry_mean','fractal_dimension_mean','radius_se','texture_se',
                      'perimeter_se','area_se','smoothness_se','compactness_se','concavity_se','concave_points_se','symmetry_se',
                      'fractal_dimension_se','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst',
                      'concavity_worst','concave_points_worst','symmetry_worst','fractal_dimension_worst']
        
        user_input = [float(x) for x in user_input]

        prediction = breast_cancer_model.predict([user_input])

        if prediction[0] == 1:
            Breast_cancer_diagnosis = "Have Breast Cancer"
        else:
            Breast_cancer_diagnosis = "The person does not have Breast Cancer"
    st.success(Breast_cancer_diagnosis)


  












 
    
  
    
    




    
