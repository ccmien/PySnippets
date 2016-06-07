import numpy as np

def unique_nested_arrays(ar):
    origin_shape = ar.shape
    origin_dtype = ar.dtype
    ar = ar.reshape(origin_shape[0], np.prod(origin_shape[1:]))
    ar = np.ascontiguousarray(ar)
    unique_ar = np.unique(ar.view([('', origin_dtype)]*np.prod(origin_shape[1:])))
    return unique_ar.view(origin_dtype).reshape((unique_ar.shape[0], ) + origin_shape[1:])
