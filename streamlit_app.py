import streamlit.components.v1 as components

# Declare the component:
my_component = components.declare_component("my_component", path="frontend/build")

# Use it:
my_component(greeting="Hello", name="World")
class MyComponent extends StreamlitComponentBase {
    public render(): ReactNode {
        // Access arguments from Python via `this.props.args`:
        const greeting = this.props.args["greeting"]
        const name = this.props.args["name"]
        return <div>{greeting}, {name}!</div>
    }
}
