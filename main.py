# HEDIYE ORHAN 09.10.2023

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import joblib
import wikipedia
import pyodbc
from nltk.stem import WordNetLemmatizer

class TextAnalyzer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stopWords = set(stopwords.words('turkish'))
        nltk.download('wordnet')
        nltk.download('omw-1.4')

    # Google Colab ortamında Egitilen yapay zeka model dosyası joblib kutuphanesi ile yuklenmistir.
    def load_model(self, model_path):
        self.model = joblib.load(model_path)

    # Yuklenen model uzerinden tahmin islemleri gerceklestirilmistir. Tahmin index numarasina gore 7 farkli kategoriden olusmaktadir.
    def predict_category(self, text):
        text2 = [text]
        pred = self.model.predict(text2)

        categories = ['Dünya', 'Ekonomi', 'Kültür - Tarih', 'Sağlık', 'Siyaset', 'Spor', 'Teknoloji']
        return categories[pred[0]]
    
    # Metnin genel konusu tahmin edildikten sonra alt konulari, anahtar kelimeleri bulunmustur. Burada metindeki kelimelerin frekansina bakilmistir.
    def find_keywords(self, text):
        text = text.lower()
        text = ''.join(e for e in text if (e.isalnum() or e.isspace()))

        words = text.split()
        word_counts = Counter(words)

        most_common_words = word_counts.most_common(2)
        keywords = " ".join(word for word, count in most_common_words)
        return keywords
    
    # Anahtar kelimeler belirlendikten sonra wikipedia sitesi uzerinden anahtar kelimelerden olusan konu basligi ile ilgili arama yapilmaktadir.
    def search_wikipedia(self, topic):
        wikipedia.set_lang("tr")
        wiki = wikipedia.page(topic)
        return wiki.content
    
    # Metindeki sayilar ve noktalama isaretleri temizlenmektedir.
    def preprocess_text(self, text):
        
        text = text.lower()
        text = ''.join(e for e in text if e.isalpha() or e.isspace())
        words = word_tokenize(text)
       
        stop_words = set(stopwords.words('turkish')) 
        words = [word for word in words if word not in stop_words]
        
        preprocessed_text = ' '.join(words)
        
        return preprocessed_text

    # Ana menu ve kullanici islemleri yonetilmektedir.
    def main_menu(self):
        server = '.'  
        database = 'hediyeorhan_nlp' 
        trusted_connection = 'yes' 
        # veri tabani baglantisi saglanmistir.
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection='+trusted_connection)

        cursor = conn.cursor()
        columns = ['content', 'topic', 'keywords']
        columns2 = ['content', 'keywords_search']
        keywords_search = ""
        while True:
            keywords = ""
            general_topic = ""
            print("\t\t -- MENU -- \n1) Metin gir\n2) Girilen metinlerin alt başliklari ile arama yap \n3) Arama konularini sifirla\n4) Çikis")
            menu = int(input("Lütfen bir seçenek seçiniz 1/2/3/4: "))

            if menu == 1:
                text = input("Lütfen bir metin giriniz: ")
                text = self.preprocess_text(text)
                general_topic = self.predict_category(text)

                
                print("\n\n --> Girilen Metnin Genel Konusu: ", general_topic)
                print("\n\n")
                keywords = self.find_keywords(text)
                data = (text, general_topic, keywords)
                keywords_search += keywords + " "
                keywords_search.strip()

                insert_query = f"INSERT INTO content_topics ({', '.join(columns)}) VALUES (?, ?, ?)"
                cursor.execute(insert_query, data)
                conn.commit()
          
            elif menu == 2:
                search_result = self.search_wikipedia(keywords_search)
                print("Araştirma yapilan anahtar kelimeler", keywords_search)
                data = (search_result, keywords_search)
                insert_query = f"INSERT INTO search ({', '.join(columns2)}) VALUES (?, ?)"
                cursor.execute(insert_query, data)
                conn.commit()
                print("\n ARASTIRMA SONUCU ELDE EDILEN BILGILER \n")
                print(search_result)
            elif  menu == 3:
                keywords_search = ""
            else:
                print("\nCikis yapiliyor ..\n")
                conn.close()
                break

if __name__ == "__main__":
    text_analyzer = TextAnalyzer()
    text_analyzer.load_model('logistic_regression_model.joblib') # onceden egitilmis yapay zeka model dosyasi
    text_analyzer.main_menu()
