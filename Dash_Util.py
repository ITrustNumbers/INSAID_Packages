
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

main_div_style = {"background-color": "#FFFFFF", "padding":"0", "width":"100%", "height":"100", "position": "fixed",
                  "top": "0%","left": "0","bottom": "0","maxHeight": "300px", 'overflowY': 'auto'}

def Callback(outputs, inputs):
  
  out_ls = []
  inp_ls = []

  for output in outputs:
    out_ls.append(Output(component_id = output, component_property = "figure"))

  for input in inputs:
    inp_ls.append(Input(component_id = input, component_property = "value"))
  return out_ls, inp_ls


def Def_Layout(children=None):

  global main_div_style

  if children is None:
    return None
  else:
    return html.Div(id = "main_div", children=children, style = main_div_style)


def Create_Graph_Canvas(n=None):

  canvas = html.Div(children = [
                            html.Div(children = [dcc.Graph(id = "bestmonth")],  
                             style = {'width': '45%', "position": "fixed", "left": "8%", 'display': 'inline-block', "background-color": "#FFFFFF", "top": "13%",}),

                            html.Div(children = [dcc.Graph(id = "store_average")],   
                             style = {'width': '45%', "position": "fixed", "left": "53%", 'display': 'inline-block', "background-color": "#FFFFFF", "top": "13%"}),

                            html.Div(children = [dcc.Graph(id = "week_sales")],     
                             style = {'width': '45%', "position": "fixed", "left": "8%", 'display': 'inline-block', "background-color": "#FFFFFF", "top": "56%",}),

                            html.Div(children = [dcc.Graph(id = "dept_average") ],
                             style = {'width': '45%', "position": "fixed", "left": "53%",'display': 'inline-block', "background-color": "#FFFFFF","top": "56%"})
                            ])
  return canvas


def Create_Dropdown_Box(id, options, default_value, style=None):

  def_style = {'width': '28%', "position": "fixed","left": "20%",'display': 'inline-block', "top": "8%", "z-index": "1"}

  if style is not None:
    for k,v in style.items():
      def_style[k] = v
  else:
    pass

  ddbox = html.Div(children = [
            dcc.Dropdown(
                    id=id,              
                    options=options,               
                    clearable=False,               
                    value = default_value,             
                    placeholder='Select a Month')],
            style = def_style)
  return ddbox