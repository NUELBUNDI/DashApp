# Import package

from dash import Dash , dcc , html # dcc .> dash core components

from datetime import date



# Get data
df = px.data.tips()

gender_type = df['sex'].unique().tolist()
time_type =        df['time'].unique().tolist()

# Create an instance of dash class
app = Dash()

# Layout

app.layout = html.Div([
    
    html.H1('Dash Core Component'), 
    html.Br(),
    
    # Drop Down
    html.H5('1 Drop Down'),
    dcc.Dropdown(options=gender_type,
                 value =gender_type[1],
                 multi= True
                 ),
    
    # Slider
    html.H5('2 Slider'),
    dcc.Slider(min  = df['total_bill'].min(), 
               max  = df['total_bill'].max(), 
               step =5
               ),
    
    # Range Slider
    html.H5('3. Range Slider'),
    dcc.RangeSlider(
        min=df['total_bill'].min(),
        max =df['total_bill'].max(),
        step = 2
    ),
    # Input 
    html.H5('4. Input'),
    dcc.Input(placeholder='Enter Your Age?',type='number'),
    
    #Text Area
    html.H5('5.Text Area'),
    dcc.Textarea(placeholder='Describe your body type'),
    
    # Check Box
    html.H5('6.Check Box'),
    dcc.Checklist(options= time_type,
                  value   = [time_type[1]],
                  inline= True
                  
                  ),
    
    
    # Date Pick
    html.H5('6.Date Picker'),
    dcc.DatePickerRange(
        start_date=date(2025,5,16)
    ),
    
    # A single date picker
    
    # 
    html.H5('6.Markdown'),
    dcc.Markdown('''
                 
                 #### Dash and Markdown
                 Dash supports markdown
                 Its simple to wrote amd format text 
                 it includes many syntax like 
                 
                        1. **Bold text**
                        2. *Italics*
                        3. links [links](https://dash.plotly.com/dash-core-components/slider)
                        4. Etc
                 
                 
                 '''
                 )
    
    

    
    
                    ])









# Run our code

if __name__ =='__main__':
    app.run(debug=True)