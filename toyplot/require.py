# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numbers
import numpy
import toyplot.compatibility

def style(style, allowed):
    if style is None:
        return style

    """Verify that the given object is usable as a style."""
    if not isinstance(style, dict):
        raise ValueError( "Expected a dictionary of CSS styles or None, received %s." % style)

    for key in style:
        if key not in allowed:
            raise ValueError("Not an allowed CSS style: %s" % key)

    return style

style.fill = set([
    "fill",
    "fill-opacity",
    "opacity",
    "stroke",
    "stroke-dasharray",
    "stroke-opacity",
    "stroke-width",
    ])

style.line = set([
    "opacity",
    "stroke",
    "stroke-dasharray",
    "stroke-opacity",
    "stroke-width",
    ])

style.marker = set([
    "fill",
    "fill-opacity",
    "opacity",
    "stroke",
    "stroke-opacity",
    "stroke-width",
    ])

style.text = set([
    "alignment-baseline",
    "baseline-shift",
    "fill",
    "fill-opacity",
    "font-size",
    "font-weight",
    "opacity",
    "stroke",
    "stroke-opacity",
    "stroke-width",
    "text-anchor",
    "-toyplot-anchor-shift",
    ])


def instance(value, types):
    """Verify the type of a value."""
    if not isinstance(value, types):
        raise ValueError("Expected %s, received %s." % (types, type(value))) #pragma: no cover
    return value


def value_in(value, choices):
    if value not in choices:
        raise ValueError("Expected one of %s, received %r." % (", ".join([repr(choice) for choice in choices]), value)) #pragma: no cover
    return value


def table_keys(table, keys, length=None, min_length=None, modulus=None):
    keys = string_vector(keys, length=length, min_length=min_length, modulus=modulus)
    allowed = list(table.keys())
    for key in keys:
        if key not in allowed:
            raise ValueError( "Table key must match one of %s, received %s." % (", ".join(allowed), key)) #pragma: no cover
    return keys

#def integer(value):
#    if not isinstance(value, numbers.Integral):
#        raise ValueError("Expected an integer, received %s." % value) #pragma: no cover
#    return value

def scalar(value):
    if not isinstance(value, numbers.Number):
        raise ValueError("Expected a number, received %s." % value) #pragma: no cover
    return value


def scalar_array(value):
    array = numpy.ma.array(value).astype("float64")
    array.mask = numpy.ma.mask_or(array.mask, ~numpy.isfinite(array))
    return array


def scalar_vector(value, length=None):
    array = scalar_array(value)
    if array.shape == ():
        array = numpy.ma.repeat(array, 1)
    if array.ndim != 1:
        raise ValueError("Expected a vector.") #pragma: no cover
    if length is not None:
        if len(array) != length:
            raise ValueError( "Expected %s values, received %s." % (length, len(array))) #pragma: no cover
    return array


def integer_array(value):
    array = numpy.ma.array(value).astype("int64")
    return array


def integer_vector(value, length=None, min_length=None):
    return vector(value, length=length, min_length=min_length).astype("int64")


def vector(value, length=None, min_length=None):
    array = numpy.ma.array(value)
    if array.shape == ():
        array = numpy.ma.repeat(array, 1)
    if array.ndim != 1:
        raise ValueError("Expected a vector.") #pragma: no cover
    if length is not None:
        if len(array) != length:
            raise ValueError( "Expected %s values, received %s" % (length, len(array))) #pragma: no cover
    if min_length is not None:
        if len(array) < min_length:
            raise ValueError( "Expected %s or more values, received %s" % (min_length, len(array))) #pragma: no cover
    return array


def scalar_matrix(value, rows=None, columns=None):
    array = scalar_array(value)
    if array.ndim != 2:
        raise ValueError("Expected a matrix.") #pragma: no cover
    if rows is not None:
        if array.shape[0] != rows:
            raise ValueError("Expected %s rows, received %s." % (rows, array.shape[0])) #pragma: no cover
    if columns is not None:
        if array.shape[1] != columns:
            raise ValueError( "Expected %s columns, received %s." % (columns, array.shape[1])) #pragma: no cover
    return array


def string(value):
    if not isinstance(value, toyplot.compatibility.string_type):
        raise ValueError("Expected a string, received %s." % value) #pragma: no cover
    return value


def string_vector(value, length=None, min_length=None, modulus=None):
    if isinstance(value, (toyplot.compatibility.string_type)):
        value = [value]
    array = numpy.ma.array(value).astype("unicode")
    if array.ndim != 1:
        raise ValueError("Expected a vector.") #pragma: no cover
    if length is not None:
        if len(array) != length:
            raise ValueError( "Expected %s values, received %s" % (length, len(array))) #pragma: no cover
    if min_length is not None:
        if len(array) < min_length:
            raise ValueError( "Expected %s or more values, received %s" % (min_length, len(array))) #pragma: no cover
    if modulus is not None:
        if len(array) % modulus != 0:
            raise ValueError( "Expected a multiple of %s values, received %s" % (modulus, len(array))) #pragma: no cover
    return array


def optional_string(value):
    if not isinstance(value, (toyplot.compatibility.string_type, type(None))):
        raise ValueError( "Expected a string value or None, received %s." % value) #pragma: no cover
    return value


def marker_array(value, length=None):
    if isinstance(value, (toyplot.compatibility.string_type, tuple)):
        array = [value] * (1 if length is None else length)
    else:
        array = value
    if length is not None:
        if len(array) != length:
            raise ValueError( "Expected %s values, received %s." % (length, len(array))) #pragma: no cover
    return array

def filename(value):
    return optional_string(value)

