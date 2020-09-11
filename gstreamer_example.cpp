#include <gst/gst.h>
#include <iostream>

using namespace std;


int main() 
{
    GstElement *pipeline, *source, *sink;
    GstBus *bus;
    GstMessage *msg;
    GstStateChangeReturn ret;


    gst_init(NULL, NULL);

    pipeline = gst_pipeline_new ("pipeline");
    source = gst_element_factory_make ("autovideosrc", "source");
    sink = gst_element_factory_make ("autovideosink", "sink");

    if (!pipeline || !source || !sink) 
    {
        cout << "not all elements created: pipeline["<< !pipeline<< "]" << "source["<< !source<< "]" << "sink["<< !sink << "]" << endl;
        return -1;
    }

    g_object_set(G_OBJECT (sink), "sync", FALSE, NULL);


    gst_bin_add_many (GST_BIN (pipeline), source, sink, NULL);
    if (gst_element_link (source, sink) != TRUE) 
    {
        cout << "Elements could not be linked." << endl;
        gst_object_unref (pipeline);
        return -1;
    }

    ret = gst_element_set_state (pipeline, GST_STATE_PLAYING);
    if (ret == GST_STATE_CHANGE_FAILURE) 
    {
        cout << "Unable to set the pipeline to the playing state." << endl;
        gst_object_unref (pipeline);
        return -1;
    }

    bus = gst_element_get_bus (pipeline);

    cout << "press CTRL + C" << endl;

    while(1);

    gst_object_unref (bus);
    gst_element_set_state (pipeline, GST_STATE_NULL);
    gst_object_unref (pipeline);
}