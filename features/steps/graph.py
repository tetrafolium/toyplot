from behave import *

import numpy
import toyplot.generate
import toyplot.layout

@given(u'a prufer tree')
def step_impl(context):
    numpy.random.seed(1234)
    context.graph = toyplot.generate.prufer_tree(numpy.random.choice(4, 12))
    context.vcoordinates = None

@given(u'a ba graph')
def step_impl(context):
    context.graph = toyplot.generate.barabasi_albert_graph(n=20)
    context.vcoordinates = None

@given(u'a default graph layout')
def step_impl(context):
    context.layout = None

@given(u'a explicit coordinates graph layout')
def step_impl(context):
    vcount = len(numpy.unique(context.graph))
    numpy.random.seed(1234)
    context.vcoordinates = numpy.random.uniform(size=(vcount, 2))
    context.layout = None

@given(u'a random graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Random()

@given(u'a eades graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Eades()

@given(u'a fruchterman-reingold graph layout')
def step_impl(context):
    context.layout = toyplot.layout.FruchtermanReingold()

@given(u'a buchheim graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Buchheim()

@given(u'a fruchterman-reingold-curved-edge graph layout')
def step_impl(context):
    context.layout = toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges())

@when(u'the graph and layout are combined')
def step_impl(context):
    context.canvas, axes, mark = toyplot.graph(context.graph, layout=context.layout, vcoordinates=context.vcoordinates)

@when(u'a graph visualization is constructed from explicit source and target edge arrays')
def step_impl(context):
    numpy.random.seed(1234)
    sources = numpy.random.choice(8, 10)
    targets = numpy.random.choice(8, 10)
    context.canvas, axes, mark = toyplot.graph(sources, targets)

@given(u'explicit source and target arrays')
def step_impl(context):
    numpy.random.seed(1234)
    context.sources = numpy.random.choice(8, 10)
    context.targets = numpy.random.choice(8, 10)

@when(u'the source and target arrays and layout are combined')
def step_impl(context):
    context.canvas, context.axes, context.mark = toyplot.graph(context.sources, context.targets, layout=context.layout)

@given(u'explicit source and target arrays with loops')
def step_impl(context):
    numpy.random.seed(1234)
    context.sources = numpy.concatenate((numpy.random.choice(8, 10), [1, 3]))
    context.targets = numpy.concatenate((numpy.random.choice(8, 10), [1, 3]))

