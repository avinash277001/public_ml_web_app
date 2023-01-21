import pickle
import streamlit as st
from streamlit_option_menu import option_menu



#Loading Saved Models
diabetes_model = pickle.load(open('Diabetes.sav', 'rb'))

Parkinsons_model = pickle.load(open('Parkinsons_Disease.sav', 'rb'))




#Sidebar for Navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System Using ML',
                           
                           ['Diabetes Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                            default_index = 0)




#Diabetes Prediction 
if(selected == 'Diabetes Prediction'):
    
    
    st.title('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnencies = st.text_input('Number of Pregnencies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunctionValue= st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of person')
    
    

    #Code For Prediction
    diabetes_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diabetes_diagnosis = diabetes_model.predict([[Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunctionValue, Age]])

        if(diabetes_diagnosis[0] == 1):
            diabetes_diagnosis = 'Person is Diabetic'
        else:
            diabetes_diagnosis = 'Person is not Diabetic'
            
    st.success(diabetes_diagnosis)



#Parkinsons Prediction
if(selected == 'Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction Using ML')


    col1, col2, col3, col4 = st.columns(4)
        
    with col1:
        fo = st.text_input('MDVP Fo(Hz)')
            
    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')
            
    with col3:
        flo = st.text_input('MDVP Flo(Hz)')
            
    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')
            
    with col1:
        Jitter_Abs = st.text_input('MDV Jitter(Abs)')
        
    with col2:
        RAP = st.text_input('MDVP RAP')
            
    with col3:
        PPQ = st.text_input('MDVP PPQ')
        
    with col4:
        DDP = st.text_input('Jitter DDP')
            
    with col1:
        Shimmer = st.text_input('MDVP Shimmer')
            
    with col2:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
            
    with col3:
        APQ3 = st.text_input('Shimmer APQ3')
            
    with col4:
        APQ5 = st.text_input('Shimmer APQ5')
            
    with col1:
        APQ = st.text_input('MDVP APQ')
            
    with col2:
        DDA = st.text_input('Shimmer DDA')
            
    with col3:
        NHR = st.text_input('NHR')
            
    with col4:
        HNR = st.text_input('HNR')
            
    with col1:
        RPDE = st.text_input('RPDE')
            
    with col2:
        DFA = st.text_input('DFA')
            
    with col3:
        Spread1 = st.text_input('Spread1')
            
    with col4:
        Spread2 = st.text_input('Spread2')
            
    with col1:
        D2 = st.text_input('D2')
            
    with col2:
        PPE = st.text_input('PPE')
            
            
            
        #Code For Prediction
        Parkinsons_diagnosis = ''
        
        if st.button('Parkinsons diagnosis Test Result'):
            Parkinsons_diagnosis = Parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]])

            if(Parkinsons_diagnosis[0] == 1):
                Parkinsons_diagnosis = "Person has Parkinson's Disease"
            else:
                Parkinsons_diagnosis = "Person has not Parkinson's Disease"
                
        st.success(Parkinsons_diagnosis)
