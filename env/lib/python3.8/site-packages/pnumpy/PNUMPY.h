
static char INITIALIZE_DOC[] = ""
"Initialize the module. Replaces all the ufunc inner loops with a new version"
"using ``PyUFunc_ReplaceLoopBySignature``. If none of the other options are"
"enabled, the original inner loop function will be called. Will also call"
"``numpy.setbufsize(8192 * 1024)`` to work around numpy issue 17649."
"";
static char ATOP_ENABLE_DOC[] = ""
"enable the atop inner loop implementations."
"";
static char ATOP_DISABLE_DOC[] = ""
"disable the atop inner loop implementations."
"";
static char ATOP_ISENABLED_DOC[] = "returns True if atop enabled, else False";
static char THREAD_ENABLE_DOC[] = ""
"Enable worker threads for inner loops when they are large enough to justify"
"the extra overhead."
"";
static char THREAD_DISABLE_DOC[] = "Disable worker threads";
static char THREAD_ISENABLED_DOC[] = "Returns True if worker threads enabled else False";
static char THREAD_GETWORKERS_DOC[] = "Get the number of worker threads";
static char THREAD_SETWORKERS_DOC[] = "Set the number of worker threads, return previous value. Must be at least 1.";
static char TIMER_GETTSC_DOC[] = "Get the time stamp counter";
static char TIMER_GETUTC_DOC[] = "Get the time in utc nanos since unix epoch";
static char CPUSTRING_DOC[] = "Cpu brand string plus features";
static char OLDINIT_DOC[] = "old, deprecated";
static char LEDGER_ENABLE_DOC[] = ""
"Enable ledger debuggging. This collects statistics on each run of a loop:"
"input signature and dimensions, time to execute the loop and more"
"";
static char LEDGER_DISABLE_DOC[] = "Disable ledger";
static char LEDGER_ISENABLED_DOC[] = "Returns True if ledger enabled else False";
static char LEDGER_INFO_DOC[] = "Return ledger information";
static char RECARRAY_TO_COLMAJOR_DOC[] = "Converts a numpy record array (void type) to a dictionary of numpy arrays, col major"
"Inputs"
"------"
"item: A numpy recorarray to return as column major"
"parallel: Default to True"
""
"Returns"
"-------"
"A dictionary of numpy arrays corresponding to the original numpy record array."
""
"Examples"
"--------"
">>> x=np.array([(1.0, 2, 3, 4, 5, 'this is a long test'), (3.0, 4, 5, 6, 7, 'short'), (30.0, 40, 50, 60, 70, '')],"
"            dtype=[('x', '<f4'), ('y', '<i2'), ('z', 'i8'),('zz','i8'),('yy','i4'),('str','<S20')])"
">>> item=np.tile(x,100_000)"
">>> mydict = recarray_to_colmajor(item)";
static char RECYCLER_ENABLE_DOC[] = "Enable recycler to compact memory usage";
static char RECYCLER_DISABLE_DOC[] = "Disable recycler";
static char RECYCLER_ISENABLED_DOC[] = "Returns True if recycler enabled else False";
static char RECYCLER_INFO_DOC[] = "Return recycler information";