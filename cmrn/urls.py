from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cancerMiRNANetwork.views.home', name='home'),
    # url(r'^cancerMiRNANetwork/', include('cancerMiRNANetwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', 'network.views.index'),
    ('^index/$', 'network.views.index'),
    ('^cancer/.*', 'network.views.cancer'),
    ('.*/bp$', 'network.views.gene_ontology'),
    ('.*/cc$', 'network.views.gene_ontology'),
    ('.*/mf$', 'network.views.gene_ontology'),
    ('.*/genes$', 'network.views.gene_listing'),
    ('^overlapping_mirna$', 'network.views.overlapping_mirna'),
    ('^overlapping_mirna_go$', 'network.views.overlapping_mirna_go'),
    ('^common_mirna_and_go_term$', 'network.views.cytoscape_web_example'),
    ('^cytoscape_web_common_mirna$', 'network.views.cytoscape_web_common_mirna'),
    ('^cytoscape_web_common_mirna_go$', 'network.views.cytoscape_web_common_mirna_go'),
    ('^inference/.*$', 'network.views.inference'),
    ('^dataset/.*$', 'network.views.dataset'),
    ('^cluster/.*$', 'network.views.cluster'),
    ('^hallmark/.*$', 'network.views.hallmark'),
    ('^hallmarks/.*$', 'network.views.hallmarks'),
    ('^miRNA/.*$', 'network.views.miRNA'),
    ('^count_em$', 'network.views.count_em'),
    ('^count_em2$', 'network.views.count_em2'),
    ('^specific_miRNA/.*$', 'network.views.specific_miRNA'),
    ('^mirna_and_go_term$', 'network.views.mirna_and_go_term'),
    ('^mirna_and_go_term_csv$', 'network.views.mirna_and_go_term_csv'),
    ('^overlapping_mirna_go_csv$', 'network.views.overlapping_mirna_go_csv'),
    ('^compendium/$', 'network.views.compendium'),
    ('^firm/$', 'network.views.firm'),
    ('^help/$', 'network.views.help_page'),
    ('^citation/$', 'network.views.citation'),
    ('^supTable8/$', 'network.views.supplementary_table_8_csv'),
    ('^supTable9/$', 'network.views.supplementary_table_9_csv'),
    ('^supTable10$', 'network.views.supplementary_table_10_csv'),
    ('^overlap/.*$', 'network.views.overlap'),
    ('^significant_overlapping_mirna_go_csv$', 'network.views.significant_overlapping_mirna_go_csv'),
    ('^hallmarks_network_sif$', 'network.views.hallmarks_network_sif'),
    ('^sig_overlap_network_sif$', 'network.views.sig_overlap_network_sif'),
    ('^all_overlapping$', 'network.views.clusters_overlapping'),
    ('^all_overlapping_hallmarks$', 'network.views.clusters_overlapping_hallmarks'),
    ('^all_overlapping_hallmarks_mir2disease$', 'network.views.clusters_overlapping_hallmarks_mir2disease'),
    ('^overlap_pita_targetscan$', 'network.views.clusters_overlapping_pita_targetscan'),
    ('^overlap_pita_targetscan_cancer$', 'network.views.clusters_overlapping_pita_targetscan_cancer'),
)
