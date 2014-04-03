# Insert Equation plugin for Sublime Text

This plugin for Sublime Text 3 offers a command to input, preview and insert a link to an image displaying a TeX formula.

The `Insert Equation as Image` command shows an input prompt where you can enter a TeX formula and a preview will be displayed while editing it.

The formulas are rendered using an online renderer that generates an image displaying the formula on the fly.
The default rendering engine is <http://latex.codecogs.com/gif.latex> but this can be changed using the `renderer` parameter.

When you are happy with the formula, by pressing enter the plugin will create the link pointing to an image showing the formula.
The actual format will be determined by the `convert_to` parameter.
If set to `"auto"` the appropriate target will be determined from the language of the current view. For example when inserting the formula into a Markdown file, the generated code will look like

    ![formula](http://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D0%7D%5En%5Cfrac%7B%5Calpha%5Ei%5B%5Ckappa%5D%28w%29%7D%7B%5Csqrt%7B%5Cbeta%7D%5Ccdot%20%5Cgamma_i%7D "\sum_{i=0}^n\frac{\alpha^i[\kappa](w)}{\sqrt{\beta}\cdot \gamma_i}")

that generates

![formula](http://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D0%7D%5En%5Cfrac%7B%5Calpha%5Ei%5B%5Ckappa%5D%28w%29%7D%7B%5Csqrt%7B%5Cbeta%7D%5Ccdot%20%5Cgamma_i%7D "\sum_{i=0}^n\frac{\alpha^i[\kappa](w)}{\sqrt{\beta}\cdot \gamma_i}")

For an alternative renderer, try
    
    "renderer": "http://chart.googleapis.com/chart?cht=tx&chl={query}"

![formula](http://chart.googleapis.com/chart?cht=tx&chl=%5Cdisplaystyle%5Csum_%7Bi%3D0%7D%5En%5Cfrac%7B%5Calpha%5Ei%5B%5Ckappa%5D%28w%29%7D%7B%5Csqrt%7B%5Cbeta%7D%5Ccdot%20%5Cgamma_i%7D "\\displaystyle\\sum\_{i=0}^n\\frac{\\alpha^i[\\kappa](w)}{\\sqrt{\\beta}\\cdot \\gamma\_i}")

The supported target formats are:

* `text` for just the url
* `md` for Markdown
* `html` for an HTML `<img>` tag
* `tex` for the TeX formula wrapped in dollars (the rendering will be done by TeX, the plugin's usefulness is in the preview)
* `source` for the url in double-quotes
* `clipboard` for copying the url in the clipboard

## MIT License

Copyright (c) 2014 Emanuele D'Osualdo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
