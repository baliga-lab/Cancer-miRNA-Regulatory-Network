from django.conf.urls import *
import network.views
#from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'cancerMiRNANetwork.views.home', name='home'),
    # url(r'^cancerMiRNANetwork/', include('cancerMiRNANetwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', network.views.index),
    url(r'^index/$', network.views.index),
    url(r'^cancer/.*', network.views.cancer),
    url(r'.*/bp$', network.views.gene_ontology),
    url(r'.*/cc$', network.views.gene_ontology),
    url(r'.*/mf$', network.views.gene_ontology),
    url(r'.*/genes$', network.views.gene_listing),
    url(r'^overlapping_mirna$', network.views.overlapping_mirna),
    url(r'^overlapping_mirna_go$', network.views.overlapping_mirna_go),
    url(r'^common_mirna_and_go_term$', network.views.cytoscape_web_example),
    url(r'^cytoscape_web_common_mirna$', network.views.cytoscape_web_common_mirna),
    url(r'^cytoscape_web_common_mirna_go$', network.views.cytoscape_web_common_mirna_go),
    url(r'^inference/.*$', network.views.inference),
    url(r'^dataset/.*$', network.views.dataset),
    url(r'^cluster/(?P<cancer>[^/]+)/(?P<cluster>\d+)$', network.views.cluster),
    url(r'^hallmark/.*$', network.views.hallmark),
    url(r'^hallmarks/.*$', network.views.hallmarks),
    url(r'^miRNA/.*$', network.views.miRNA),
    url(r'^count_em$', network.views.count_em),
    url(r'^count_em2$', network.views.count_em2),
    url(r'^specific_miRNA/.*$', network.views.specific_miRNA),
    url(r'^mirna_and_go_term$', network.views.mirna_and_go_term),
    url(r'^mirna_and_go_term_csv$', network.views.mirna_and_go_term_csv),
    url(r'^overlapping_mirna_go_csv$', network.views.overlapping_mirna_go_csv),
    url(r'^compendium/$', network.views.compendium),
    url(r'^firm/$', network.views.firm),
    url(r'^help/$', network.views.help_page),
    url(r'^citation/$', network.views.citation),
    url(r'^supTable8/$', network.views.supplementary_table_8_csv),
    url(r'^supTable9/$', network.views.supplementary_table_9_csv),
    url(r'^supTable10$', network.views.supplementary_table_10_csv),
    url(r'^overlap/.*$', network.views.overlap),
    url(r'^significant_overlapping_mirna_go_csv$', network.views.significant_overlapping_mirna_go_csv),
    url(r'^hallmarks_network_sif$', network.views.hallmarks_network_sif),
    url(r'^sig_overlap_network_sif$', network.views.sig_overlap_network_sif),
    url(r'^all_overlapping$', network.views.clusters_overlapping),
    url(r'^all_overlapping_hallmarks$', network.views.clusters_overlapping_hallmarks),
    url(r'^all_overlapping_hallmarks_mir2disease$', network.views.clusters_overlapping_hallmarks_mir2disease),
    url(r'^overlap_pita_targetscan$', network.views.clusters_overlapping_pita_targetscan),
    url(r'^overlap_pita_targetscan_cancer$', network.views.clusters_overlapping_pita_targetscan_cancer),
]
