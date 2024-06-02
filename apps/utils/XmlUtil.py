from lxml import etree
from lxml.etree import _Element
from signxml import XMLSigner, methods

from config.settings import BASE_DIR


class XmlUtil:

    @staticmethod
    def remove_tags_empty(xml) -> str:
        root = etree.fromstring(xml)
        for element in root.xpath(".//*[not(node())]"):
            element.getparent().remove(element)
        return etree.tostring(root, encoding='utf8')

    @staticmethod
    def add_attr_tag(xml, tag_name: str, attr_name: str, attr_value: str) -> str:
        root = etree.fromstring(xml)
        for element in root.findall(tag_name):
            element.set(attr_name, attr_value)

        return etree.tostring(root, encoding='utf8')

    @staticmethod
    def add_signature(xml: str, xpath: str):
        root = etree.fromstring(xml)
        for element in root.findall(xpath):
            # Assinar cada tag <child>
            signed_child = XmlUtil.generate_signature(element)

            # Substituir a tag original pela assinada no documento
            if (parent := element.getparent()) is not None:
                parent.replace(element, signed_child)
            else:
                root = signed_child

        return etree.tostring(root, encoding='utf8')

    @staticmethod
    def generate_signature(root: _Element) -> _Element:
        signer = XMLSigner(method=methods.enveloped, digest_algorithm='sha256')
        # root = etree.fromstring(xml)
        cert = open(BASE_DIR / 'apps' / 'utils' / 'certificate.pem').read()
        key = open(BASE_DIR / 'apps' / 'utils' / 'private_key.pem').read()

        signed_root = signer.sign(root, key=key, cert=cert)

        return signed_root

    @staticmethod
    def to_string(xml: str | bytes):
        return xml if isinstance(xml, str) else xml.decode('utf8')
