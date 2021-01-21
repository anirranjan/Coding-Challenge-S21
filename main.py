from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

record = SeqIO.read("Genome.gb", "genbank")

#creating empty diagram, empty track, and empty feature set
gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name = "Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

#taking each gene in record and generating feature on the diagram
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue
    gd_feature_set.add_feature(feature, color = color, label = True, label_size = 14, label_angle = 0)

#making output file
gd_diagram.draw(
    format = "circular",
    circular = True,
    pagesize = (20 * cm, 20 * cm),
    start = 0,
    end = len(record),
    circle_core = 0.7,
)
gd_diagram.write("genome_map.png", "PNG") 
