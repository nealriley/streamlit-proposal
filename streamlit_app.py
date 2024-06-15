import streamlit as st
from streamlit_p5 import sketch

st.set_page_config(layout="wide")

st.title("Streamlit's Evolution")

st.info("""
This is a brief by the Adaptavist Group on the opportunities we see in the Streamlit ecosystem.

This includes: 

- Making the most out of the kinetic web through WebGPU/Canvas, and htmx
- The deeper integration with the activities and experiences that LLMs enable
- Enabling a B2B ecosystem through App building and Component commercialization
""", icon="ℹ️")

"""
---

Streamlit represents a huge potential for future growth, as it is uniquely placed to capture the creativity and analysis Streamlit creators produce today, and bring new forms of engagement, new customers to serve, and new ecosystems they can operate in.

---

## Adopting the Kinetic Web

The dream of Web 2.0 was moving from static to responsive content. This includes the ability for a user to submit information, and perform "asynchronous" operations via JavaScript (remember AJAX?), but it also includes a number of elements in the HTML spec that allow for different modes of operation beyond strictly textual/static design.

This includes the Canvas element, and other audio and video capabilities. As with other similar technologies in other platforms/standards, developing "web apps" that operate more like a visual game engine can be quite complicated.

There are a number of libraries over the years that have emerged to approach this space, and one that did a great job to lower the barrier to entry for developers to build simple 'sketches' was the Processing community. Specifically, the [ProcessingJS](https://www.p5js.org) library does a great job of this. I love it so much, we put together a quick sample component embedding it!

"""
"""Get started by installing streamlit-p5:"""
st.code("""
pip install streamlit-p5
""")
"""_sketch.py_"""
st.code("""        
import streamlit as st
from streamlit_p5 import sketch
        
sketch('''
let name="Let's be playful"; 
function setup() { 
  createCanvas(700, 500); 
  textSize(54)
  fill(255);
} 
function draw() { 
  background(14,17,23); 
  text(name, width / 8, mouseY); 
}
''', width=900, height=500)""")

sketch('''
let name="Let's be playful"; 
function setup() { 
  createCanvas(700, 500); 
  textSize(54)
  fill(255);
} 
function draw() { 
  background(14,17,23); 
  text(name, width / 8, mouseY); 
}
''', width=900, height=500)

"""
Due to the power of the component ecosystem in Streamlit, and the fact that P5 is a DSL on top of JavaScript/HTML at its core, the ability to deeply integrate this kind of capability in Streamlit is at hand. With the ability to move data in and out of Streamlit's Python infrastructure, the number of new experiences a Streamlit creator can make are infinitely increased. The ability to create a new kind of "app" that is more like a game, or a visualizer, or a simulation, is now at hand. There are other possible areas of expansion here using the same core components, such as the work of [ThreeJS](https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language) in the world of Data Experiences and other kinetic web experiences.

Likewise, the integration of Streamlit into an experience that is usable as an App, either in the iOS or Android ecosystems, represents another key deployment model that could grow the market addressable by Streamlit. It also allows for in-app integrations (e.g., App Intents in iOS) that intersect Streamlit into the flow of end-users' daily tasks.

"""

st.header("Becoming the network for LLM exploration")

"""
The LLM (Large Language Model) ecosystem is a new and emerging space that is growing rapidly. The ability to create a "low code" experience that is more like a "no code" experience is a key enabler for the next generation of creators. The integration of LLMs into Streamlit can simplify the development process by allowing users to leverage natural language for coding, querying, and generating content.

LLMs can enhance Streamlit applications by providing advanced language understanding and generation capabilities. This can lead to more intuitive user interfaces, automated content creation, and real-time data analysis. The combination of LLMs with Streamlit's interactive components can create powerful tools for education, business intelligence, and creative projects.

Moreover, the potential for LLMs to assist in code generation and debugging can significantly reduce development time and lower the barrier to entry for non-programmers. By integrating LLMs, Streamlit can become a central hub for AI-driven applications, empowering users to build sophisticated solutions with minimal effort.

"""

"""
## Enabling a B2B Ecosystem through App Building and Component Commercialization

Streamlit's flexibility and ease of use make it an ideal platform for building custom applications tailored to specific business needs. By enabling a B2B ecosystem, Streamlit can facilitate the creation of specialized tools and services that cater to various industries, enhancing productivity and operational efficiency.

### Custom Application Development

Businesses can leverage Streamlit to develop bespoke applications that address their unique challenges. Whether it's a data visualization dashboard, a machine learning model interface, or a workflow automation tool, Streamlit's interactive components and Python integration make it possible to build powerful applications quickly and efficiently. This capability allows businesses to respond to market demands rapidly and stay competitive.

### Component Commercialization

One of the most exciting opportunities within the Streamlit ecosystem is the potential for component commercialization. Developers can create reusable components that can be integrated into various Streamlit applications. These components, which can be built using raw HTML, React, Vite, or other deployment patterns, offer a modular approach to app development.

By leveraging platforms like Salable, developers can monetize their components, creating a marketplace for paid-for components. This not only provides a revenue stream for developers but also enriches the Streamlit ecosystem with high-quality, specialized components that can be easily integrated into new or existing applications.

### Benefits of a Component Marketplace

1. **Quality and Innovation**: A marketplace incentivizes developers to create high-quality, innovative components that meet the needs of businesses across different sectors.
2. **Cost Efficiency**: Businesses can save on development costs by purchasing ready-made components instead of building them from scratch.
3. **Speed to Market**: With access to a wide range of components, businesses can accelerate their development cycles and bring solutions to market faster.
4. **Support and Updates**: Commercial components often come with support and regular updates, ensuring that they remain functional and secure over time.

Enabling a B2B ecosystem through app building and component commercialization positions Streamlit as a central player in the enterprise application landscape. By fostering a marketplace for paid-for components, Streamlit can drive innovation, reduce development costs, and accelerate time-to-market for businesses. This strategic direction not only benefits developers and businesses but also strengthens the overall Streamlit ecosystem.
"""