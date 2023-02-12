#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install speedtest-cli


# In[2]:


import speedtest

st = speedtest.Speedtest()

# Escolhendo o melhor servidor para teste
st.get_best_server()

# Verificando a velocidade de download
download_speed = st.download()

# Verificando a velocidade de upload
upload_speed = st.upload()

# Mostrando a velocidade de download e upload
print("Download speed: %.2f Mbps" % (download_speed / 1e6))
print("Upload speed: %.2f Mbps" % (upload_speed / 1e6))


# In[ ]:




