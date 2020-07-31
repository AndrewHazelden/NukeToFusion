"""
Import all effects from the nodes folder to allow them to be easily called from
other scripts using the node's effect type attribute.
"""

from nusion.model.nodes.nuke_to_fusion import   BaseAttributes, \
                                                CommonAttributes, \
                                                Blur, \
                                                ColorCorrect, \
                                                Transform, \
                                                Invert

def convert(node):
    """ List of effect conversion functions """

    base_attribs = BaseAttributes.convert(node)
    common_attribs = CommonAttributes.convert(node)

    if node.effect == "Blur":
        return base_attribs, {**common_attribs, **Blur.convert(node)}

    if node.effect == "ColorCorrect":
        return base_attribs, {**common_attribs, **ColorCorrect.convert(node)}

    if node.effect == "Transform":
        return base_attribs, {**common_attribs, **Transform.convert(node)}

    if node.effect == "Invert":
        return base_attribs, {**common_attribs, **Invert.convert(node)}

    raise ValueError("Node effect '{0}' not currently supported.".format(node.effect))
