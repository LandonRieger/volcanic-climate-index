from bokeh.models.widgets import Div


def vci_text(width, height=None):

    div = Div(text=
              """<p>Volcanic eruptions have had major and sporadic impacts on the climate system, reducing temperatures, 
              changing circulation patterns and affecting stratospheric chemistry; but the magnitude of this impact varies 
              widely between eruptions. Effects depend not only on the amount of ash and sulfur injected into the 
              stratosphere, but also the timing and placement of the eruption relative to the atmospheric state. Eruptions 
              at higher latitudes reach the stratosphere more easily, while the phase of the QBO affects the confinement 
              of aerosol in the tropics to name just two. While countless eruptions have occurred in the past decades and 
              centuries, only a small fraction of these have had substantial climate effects. Quantifying what eruptions 
              have an impact and their relative magnitude is a complex problem and one that has been approached from 
              different directions in the past.</p>
              
            <p>In 1982 Newhall and Self introduced the Volcanic Explosivity Index (VEI) to help evaluate records of 
            past volcanic eruptions. Based largely on the volume of tephra emitted by the eruption, VEI has been 
            calculated for most modern and many of the larger past eruptions, making for a long term and up-to-date 
            database for comparison. In the climate community, this metric is often used as a proxy to indicate eruptions 
            with marked impact on global temperatures. However, the correlation between climate variables such as 
            temperature and VEI are poor, as it does not directly incorporate sulfur emissions, residence time in the 
            atmosphere, or indirect effects. Since VEI, other metrics have emerged to address these concerns, such as 
            the Volcanic Sulfur Dioxide Index (VSI) which is based on the total sulfur emitted to the stratosphere. 
            While more direct than VEI, these improvements still leave possibly important effects unaccounted for, and 
            the metrics have not been widely adopted.</p>
            
            <p>This work seeks an improved metric that better describes a volcanic eruptions’ impact on climate by 
            answering the following questions:
            <ul>
            <li>What variables best define “climate impact?” Temperature, radiative forcing, circulation changes, etc.</li>
            <li>What metric can be quickly and easily determined after an eruption that captures these variables?</li>
            <li>What metric can be applied to both past and present eruptions with vastly different observational data?</li>
            </ul>
            </p>""",
    width=width)
    return div