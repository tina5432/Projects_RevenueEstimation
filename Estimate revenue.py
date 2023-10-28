#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

appointments_df = pd.read_csv('C:/Users/Dell/Desktop/JOB/p21_bi_intern_test_appointments.csv')
revenues_df = pd.read_csv('C:/Users/Dell/Desktop/JOB/p21_bi_intern_test_revenues.csv')


# In[14]:


merged_df = pd.merge(appointments_df, revenues_df, on='appointment_id')


# In[15]:


income = merged_df.groupby('clinic_id')['revenues'].sum()


# In[16]:


unique_patients = merged_df.groupby('clinic_id')['patient_id'].nunique()


# In[17]:


existing_income = income * 12/12
existing_unique_patients = unique_patients * 12/12

new_clinic1_income = income * 9/12
new_clinic1_unique_patients = unique_patients * 9/12

new_clinic2_income = income * 5/12
new_clinic2_unique_patients = unique_patients * 5/12

total_income = existing_income + new_clinic1_income + new_clinic2_income
total_unique_patients = existing_unique_patients + new_clinic1_unique_patients + new_clinic2_unique_patients


# In[18]:


print("Estimated Revenues for 2023:", total_income)


# In[19]:


print("Estimated Unique Patients for 2023:", total_unique_patients)


# In[ ]:




