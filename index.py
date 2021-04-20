from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#---------------HOME---------------
@app.route('/java')
def java():
    return render_template('java.html')

@app.route('/python')
def python():
    return render_template('wop.html') #En proceso, se sube cuando este acabada
    #return render_template('python.html')
    
@app.route('/android')
def android():
    return render_template('android.html')

@app.route('/javaScript')
def javaScript():
    return render_template('wop.html') #En proceso, se sube cuando este acabada
    #return render_template('javaScript.html')

@app.route('/about')
def about():
    return render_template('wop.html') #En proceso, se sube cuando este acabada
    #return render_template('about.html')

#---------------JAVA---------------
    #---GestHotel------------------
@app.route('/java/hotel')
def hotel():
    return render_template('java/gestHotel.html')

@app.route('/java/hotel/app')
def gestHotel():
    return redirect('https://rgg-gesthotel.herokuapp.com/')

@app.route('/java/hotel/src') 
def srcGestHotel():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return redirect('http://')

    
    #---GestAulas------------------
@app.route('/java/aulas')
def aulas():
    return render_template('java/gestAulas.html')

@app.route('/java/aulas/app')
def gestAulas():
    return redirect('http://rgg-gestaulas.herokuapp.com/login')

@app.route('/java/aulas/src')
def srcGestAulas():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return redirect('http://')


#---------------PYTHON-------------
    #---DescargaYt-----------------
@app.route('/python/descargaYt')
def descargaYt():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return render_template('python/descargaYt.html')



#---------------ANDROID------------
    #---Fitmed---------------------
@app.route('/android/fitMed')
def fitMed():
    return render_template('android/fitMed.html')

@app.route('/android/fitMed/src')
def srcFitMed():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return redirect('http://')


    #---GestAulas-Mobile-----------
@app.route('/android/gestAulasMobile')
def gestAulasMobile():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return render_template('android/gestAulasMobile.html')

@app.route('/android/gestAulasMobile/src')
def srcGestAulasMobile():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return redirect('http://')


    #---GesTension-----------------
@app.route('/android/gesTension')
def gesTension():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return render_template('android/gesTension.html')

@app.route('/android/gesTension/src')
def srcGesTension():
    return render_template('wop.html')  #En proceso, se sube cuando este acabada
    #return redirect('http://')


    
    


#---------------JAVASCRIPT----------


if __name__ == '__main__':
    app.run(debug=True)