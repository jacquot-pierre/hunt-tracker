from lxml import etree
from logging import getLogger, StreamHandler

logger = getLogger(__name__)
logger.setLevel("DEBUG")

# Also log to console.
console = StreamHandler()
logger.addHandler(console)

class huntAttributes():
    def __init__(self, path_to_xml) -> None:
        self._path_to_xml = path_to_xml  # Path to the XML file
        self.tree = etree.parse(self._path_to_xml)  # Parse the XML file

# Create main function
def main():
    # Create object
    hunt_attributes = huntAttributes(path_to_xml="F:\\SteamLibrary\\steamapps\\common\\Hunt Showdown\\user\\profiles\\default\\attributes.xml")
    import IPython; IPython.embed()  # Start IPython shell
    # Print the object
    logger.info(hunt_attributes)

if __name__ == "__main__":
    main()