from . import comms, io, obs, opengl, poses, rtti, system, typemeta
from . import apps, bayes, config, containers, cpu, expr, global_settings
from . import graphs, gui, hwdrivers, img, kinematics, maps, math, nav
from . import random, serialization, slam, tfest, topography, vision


from typing import Any, ClassVar, List

from typing import overload

class Clock:
    class Source:
        __doc__: ClassVar[str] = ...  # read-only
        __members__: ClassVar[dict] = ...  # read-only
        Monotonic: ClassVar[Clock.Source] = ...
        Realtime: ClassVar[Clock.Source] = ...
        Simulated: ClassVar[Clock.Source] = ...
        __entries: ClassVar[dict] = ...
        def __init__(self, value: int) -> None: ...
        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    Monotonic: ClassVar[Clock.Source] = ...
    Realtime: ClassVar[Clock.Source] = ...
    Simulated: ClassVar[Clock.Source] = ...
    def __init__(self) -> None: ...
    def fromDouble(self, *args, **kwargs) -> Any: ...
    def getActiveClock(self, *args, **kwargs) -> Any: ...
    def getMonotonicToRealtimeOffset(self, *args, **kwargs) -> Any: ...
    def now(self, *args, **kwargs) -> Any: ...
    def nowDouble(self, *args, **kwargs) -> Any: ...
    def resetMonotonicToRealTimeEpoch(self, *args, **kwargs) -> Any: ...
    def setActiveClock(self, *args, **kwargs) -> Any: ...
    def setSimulatedTime(self, *args, **kwargs) -> Any: ...
    def toDouble(self, *args, **kwargs) -> Any: ...

class Stringifyable:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Stringifyable) -> None: ...
    def asString(self) -> str: ...
    def assign(self) -> Stringifyable: ...

class TCallStackBackTrace:
    backtrace_levels: List[TCallStackEntry]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: TCallStackBackTrace) -> None: ...
    def asString(self) -> str: ...
    def assign(self) -> TCallStackBackTrace: ...

class TCallStackEntry:
    sourceFileFullPath: str
    sourceFileName: str
    sourceFileNumber: int
    symbolName: str
    symbolNameOriginal: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: TCallStackEntry) -> None: ...
    def assign(self) -> TCallStackEntry: ...

class WorkerThreadsPool:
    class queue_policy_t:
        __doc__: ClassVar[str] = ...  # read-only
        __members__: ClassVar[dict] = ...  # read-only
        POLICY_DROP_OLD: ClassVar[WorkerThreadsPool.queue_policy_t] = ...
        POLICY_FIFO: ClassVar[WorkerThreadsPool.queue_policy_t] = ...
        __entries: ClassVar[dict] = ...
        def __init__(self, value: int) -> None: ...
        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    POLICY_DROP_OLD: ClassVar[WorkerThreadsPool.queue_policy_t] = ...
    POLICY_FIFO: ClassVar[WorkerThreadsPool.queue_policy_t] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, num_threads: int) -> None: ...
    @overload
    def __init__(self, num_threads: int, p) -> None: ...
    @overload
    def __init__(self, num_threads: int, p, threadsName: str) -> None: ...
    @overload
    def clear(self) -> None: ...
    @overload
    def clear() -> void: ...
    @overload
    def name(self, name: str) -> None: ...
    @overload
    def name(conststd) -> void: ...
    @overload
    def name(self) -> str: ...
    def pendingTasks(self) -> int: ...
    @overload
    def resize(self, num_threads: int) -> None: ...
    @overload
    def resize(std) -> void: ...
    def size(self) -> int: ...

class ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t) -> None: ...
    @overload
    def __init__(self, p, octomap) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, p, octomap) -> ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t: ...
    @overload
    def assign(self) -> ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def set(self, p, octomap) -> None: ...
    @overload
    def set(constclassmrpt, classoctomap) -> void: ...
    @overload
    def __eq__(self, o, octomap) -> bool: ...
    @overload
    def __eq__(self, o: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t) -> bool: ...
    @overload
    def __ne__(self, o, octomap) -> bool: ...
    @overload
    def __ne__(self, o: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_ColorOcTree_octomap_ColorOcTreeNode_t) -> bool: ...

class ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t) -> None: ...
    @overload
    def __init__(self, p, octomap) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, p, octomap) -> ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t: ...
    @overload
    def assign(self) -> ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def set(self, p, octomap) -> None: ...
    @overload
    def set(constclassmrpt, classoctomap) -> void: ...
    @overload
    def __eq__(self, o, octomap) -> bool: ...
    @overload
    def __eq__(self, o: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t) -> bool: ...
    @overload
    def __ne__(self, o, octomap) -> bool: ...
    @overload
    def __ne__(self, o: ignored_copy_ptr_mrpt_maps_COctoMapBase_octomap_OcTree_octomap_OcTreeNode_t) -> bool: ...

class int_select_by_bytecount_1U_t:
    def __init__(self) -> None: ...

class int_select_by_bytecount_2U_t:
    def __init__(self) -> None: ...

class int_select_by_bytecount_3U_t:
    def __init__(self) -> None: ...

class int_select_by_bytecount_4U_t:
    def __init__(self) -> None: ...

class int_select_by_bytecount_8U_t:
    def __init__(self) -> None: ...

class non_copiable_ptr_basic_void_t:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: non_copiable_ptr_basic_void_t) -> None: ...
    @overload
    def __init__(self, p: capsule) -> None: ...
    def arrow(self) -> capsule: ...
    @overload
    def assign(self, p: capsule) -> non_copiable_ptr_basic_void_t: ...
    @overload
    def assign(self) -> non_copiable_ptr_basic_void_t: ...
    def get(self) -> capsule: ...
    def set(self, p: capsule) -> None: ...
    @overload
    def __eq__(self, o: capsule) -> bool: ...
    @overload
    def __eq__(self, o: non_copiable_ptr_basic_void_t) -> bool: ...
    @overload
    def __ne__(self, o: capsule) -> bool: ...
    @overload
    def __ne__(self, o: non_copiable_ptr_basic_void_t) -> bool: ...

class ptr_cast_mrpt_serialization_CSerializable_t:
    def __init__(self) -> None: ...
    def from(self, *args, **kwargs) -> Any: ...

class safe_ptr_basic_mrpt_opengl_Scene_t:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: safe_ptr_basic_mrpt_opengl_Scene_t) -> None: ...
    @overload
    def __init__(self, p) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, p) -> safe_ptr_basic_mrpt_opengl_Scene_t: ...
    @overload
    def assign(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> safe_ptr_basic_mrpt_opengl_Scene_t: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def __eq__(self, o) -> bool: ...
    @overload
    def __eq__(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> bool: ...
    @overload
    def __ne__(self, o) -> bool: ...
    @overload
    def __ne__(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> bool: ...

class safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> None: ...
    @overload
    def __init__(self, p) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, p) -> safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t: ...
    @overload
    def assign(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def __eq__(self, o) -> bool: ...
    @overload
    def __eq__(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> bool: ...
    @overload
    def __ne__(self, o) -> bool: ...
    @overload
    def __ne__(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> bool: ...

class safe_ptr_mrpt_opengl_Scene_t(safe_ptr_basic_mrpt_opengl_Scene_t):
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: safe_ptr_mrpt_opengl_Scene_t) -> None: ...
    @overload
    def __init__(self, p) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, o: safe_ptr_mrpt_opengl_Scene_t) -> safe_ptr_mrpt_opengl_Scene_t: ...
    @overload
    def assign(self, p) -> safe_ptr_mrpt_opengl_Scene_t: ...
    @overload
    def assign(self, p) -> safe_ptr_basic_mrpt_opengl_Scene_t: ...
    @overload
    def assign(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> safe_ptr_basic_mrpt_opengl_Scene_t: ...
    def dereference(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def __eq__(self, o) -> bool: ...
    @overload
    def __eq__(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> bool: ...
    def __getitem__(self, index) -> Any: ...
    @overload
    def __ne__(self, o) -> bool: ...
    @overload
    def __ne__(self, o: safe_ptr_basic_mrpt_opengl_Scene_t) -> bool: ...

class safe_ptr_mrpt_rtti_TRuntimeClassId_t(safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t):
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: safe_ptr_mrpt_rtti_TRuntimeClassId_t) -> None: ...
    @overload
    def __init__(self, p) -> None: ...
    def arrow(self, *args, **kwargs) -> Any: ...
    @overload
    def assign(self, o: safe_ptr_mrpt_rtti_TRuntimeClassId_t) -> safe_ptr_mrpt_rtti_TRuntimeClassId_t: ...
    @overload
    def assign(self, p) -> safe_ptr_mrpt_rtti_TRuntimeClassId_t: ...
    @overload
    def assign(self, p) -> safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t: ...
    @overload
    def assign(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t: ...
    def dereference(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    @overload
    def __eq__(self, o) -> bool: ...
    @overload
    def __eq__(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> bool: ...
    def __getitem__(self, index) -> Any: ...
    @overload
    def __ne__(self, o) -> bool: ...
    @overload
    def __ne__(self, o: safe_ptr_basic_mrpt_rtti_TRuntimeClassId_t) -> bool: ...

class uint_select_by_bytecount_1U_t:
    def __init__(self) -> None: ...

class uint_select_by_bytecount_2U_t:
    def __init__(self) -> None: ...

class uint_select_by_bytecount_3U_t:
    def __init__(self) -> None: ...

class uint_select_by_bytecount_4U_t:
    def __init__(self) -> None: ...

class uint_select_by_bytecount_8U_t:
    def __init__(self) -> None: ...

@overload
def DEG2RAD(x: float) -> float: ...
@overload
def DEG2RAD(constdouble) -> double: ...
@overload
def DEG2RAD(x: float) -> float: ...
@overload
def DEG2RAD(constfloat) -> float: ...
@overload
def DEG2RAD(x: int) -> float: ...
@overload
def DEG2RAD(constint) -> double: ...
@overload
def DEG2RAD(x: float) -> float: ...
@overload
def DEG2RAD(constlongdouble) -> longdouble: ...
@overload
def RAD2DEG(x: float) -> float: ...
@overload
def RAD2DEG(constdouble) -> double: ...
@overload
def RAD2DEG(x: float) -> float: ...
@overload
def RAD2DEG(constfloat) -> float: ...
@overload
def RAD2DEG(x: float) -> float: ...
@overload
def RAD2DEG(constlongdouble) -> longdouble: ...
def aligned_calloc(bytes: int, alignment: int) -> capsule: ...
def aligned_free(ptr: capsule) -> None: ...
def aligned_malloc(size: int, alignment: int) -> capsule: ...
@overload
def callStackBackTrace(out_bt: TCallStackBackTrace) -> None: ...
@overload
def callStackBackTrace(out_bt: TCallStackBackTrace, framesToSkip: int) -> None: ...
@overload
def callStackBackTrace(out_bt: TCallStackBackTrace, framesToSkip: int, framesToCapture: int) -> None: ...
@overload
def callStackBackTrace() -> TCallStackBackTrace: ...
@overload
def callStackBackTrace(framesToSkip: int) -> TCallStackBackTrace: ...
@overload
def callStackBackTrace(framesToSkip: int, framesToCapture: int) -> TCallStackBackTrace: ...
@overload
def d2f(d: float) -> float: ...
@overload
def d2f(constdouble) -> float: ...
@overload
def f2u8(f: float) -> int: ...
@overload
def f2u8(constfloat) -> uint8_t: ...
def hypot_fast(x: float, y: float) -> float: ...
@overload
def keep_max(var: float, test_val: float) -> None: ...
@overload
def keep_max(var: float, test_val: float) -> None: ...
@overload
def keep_max(var: float, test_val: float) -> None: ...
@overload
def keep_min(var: float, test_val: float) -> None: ...
@overload
def keep_min(var: float, test_val: float) -> None: ...
@overload
def keep_min(var: float, test_val: float) -> None: ...
@overload
def round(value: float) -> int: ...
@overload
def round(constfloat) -> int: ...
@overload
def round(value: float) -> int: ...
@overload
def round(constdouble) -> int: ...
@overload
def sign(x: float) -> int: ...
@overload
def sign(double) -> int: ...
@overload
def signWithZero(x: float) -> int: ...
@overload
def signWithZero(double) -> int: ...
@overload
def square(x: float) -> float: ...
@overload
def square(constdouble) -> double: ...
@overload
def square(x: float) -> float: ...
@overload
def square(constfloat) -> float: ...
@overload
def toNativeEndianness(v_in: int) -> int: ...
@overload
def toNativeEndianness(v_in: int) -> int: ...
@overload
def to_string(v: float) -> str: ...
@overload
def to_string(v: int) -> str: ...
@overload
def to_string(v: int) -> str: ...
@overload
def to_string(v: int) -> str: ...
@overload
def to_string(v: float) -> str: ...
@overload
def to_string(v: str) -> str: ...
@overload
def to_string(v: bool) -> str: ...
@overload
def to_string(s: str) -> str: ...
@overload
def u8tof(v: int) -> float: ...
@overload
def u8tof(constunsignedchar) -> float: ...