def generate_neural_network_svg():
    import xml.etree.ElementTree as ET
    import os

    # Get user input for the number of layers and nodes in each layer
    num_layers = int(input("Enter the number of layers: "))
    layers = []
    for i in range(num_layers):
        num_nodes = int(input(f"Enter the number of nodes in layer {i + 1}: "))
        layers.append(num_nodes)

    # Get user input for file name, node color, connection color, and line width
    file_name = input("Enter the file name (without .svg extension): ")
    node_color = input("Enter the node color (e.g., skyblue): ")
    connection_color = input("Enter the connection color (e.g., black): ")
    line_width = input("Enter the connection line width (e.g., 1): ")

    # Define some constants for the SVG diagram
    width = 800
    height = 100 * max(layers)
    node_radius = 20
    layer_spacing = 200
    node_spacing = 100

    # Create the root SVG element
    svg = ET.Element('svg', width=str(width), height=str(height), xmlns="http://www.w3.org/2000/svg")

    # Function to create a circle (node)
    def create_circle(cx, cy, r, fill, stroke):
        return ET.Element('circle', cx=str(cx), cy=str(cy), r=str(r), fill=fill, stroke=stroke)

    # Function to create a line (connection)
    def create_line(x1, y1, x2, y2, stroke, stroke_width):
        return ET.Element('line', x1=str(x1), y1=str(y1), x2=str(x2), y2=str(y2), stroke=stroke, **{'stroke-width': stroke_width})

    # Calculate the positions of the nodes
    positions = []
    for i, nodes in enumerate(layers):
        layer_positions = []
        x = layer_spacing * i + 50
        y_spacing = height / (nodes + 1)
        for j in range(nodes):
            y = y_spacing * (j + 1)
            layer_positions.append((x, y))
        positions.append(layer_positions)

    # Create the connections first to ensure nodes are in front
    for i, layer_positions in enumerate(positions):
        if i < len(positions) - 1:
            for x, y in layer_positions:
                for next_x, next_y in positions[i + 1]:
                    line = create_line(x, y, next_x, next_y, connection_color, line_width)
                    svg.append(line)

    # Create the nodes
    for layer_positions in positions:
        for x, y in layer_positions:
            node = create_circle(x, y, node_radius, node_color, stroke=connection_color)
            svg.append(node)

    # Convert the ElementTree to a string
    svg_str = ET.tostring(svg, encoding='unicode')

    # Save the SVG string to a file
    file_path = os.path.join(os.getcwd(), f"SVG files/{file_name}.svg")
    with open(file_path, "w") as file:
        file.write(svg_str)

    print(f"SVG file saved as {file_path}")


# Example usage
generate_neural_network_svg()
