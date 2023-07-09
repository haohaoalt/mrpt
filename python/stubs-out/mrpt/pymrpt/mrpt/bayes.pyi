from typing import Any, ClassVar

from typing import overload
import mrpt.pymrpt.mrpt.config
import mrpt.pymrpt.mrpt.math
import mrpt.pymrpt.mrpt.system
kfEKFAlaDavison: TKFMethod
kfEKFNaive: TKFMethod
kfIKF: TKFMethod
kfIKFFull: TKFMethod

class CKalmanFilterCapable_3UL_2UL_2UL_3UL_double_t:
    def __init__(self, *args, **kwargs) -> None: ...
    def OnNewLandmarkAddedToMap(self, in_obsIdx: int, in_idxNewFeat: int) -> None: ...
    @overload
    def OnNormalizeStateVector(self) -> None: ...
    @overload
    def OnNormalizeStateVector() -> void: ...
    @overload
    def OnPostIteration(self) -> None: ...
    @overload
    def OnPostIteration() -> void: ...
    def getLandmarkCov(self, idx: int, feat_cov: mrpt.pymrpt.mrpt.math.CMatrixFixed_double_2UL_2UL_t) -> None: ...
    def getLandmarkMean(self, idx: int, feat: mrpt.pymrpt.mrpt.math.CMatrixFixed_double_2UL_1UL_t) -> None: ...
    @overload
    def getNumberOfLandmarksInTheMap(self) -> int: ...
    @overload
    def getNumberOfLandmarksInTheMap() -> size_t: ...
    def getProfiler(self) -> mrpt.pymrpt.mrpt.system.CTimeLogger: ...
    @overload
    def getStateVectorLength(self) -> int: ...
    @overload
    def getStateVectorLength() -> size_t: ...
    def get_action_size(self, *args, **kwargs) -> Any: ...
    def get_feature_size(self, *args, **kwargs) -> Any: ...
    def get_observation_size(self, *args, **kwargs) -> Any: ...
    def get_vehicle_size(self, *args, **kwargs) -> Any: ...
    def internal_getPkk(self) -> mrpt.pymrpt.mrpt.math.CMatrixDynamic_double_t: ...
    def internal_getXkk(self, *args, **kwargs) -> Any: ...
    @overload
    def isMapEmpty(self) -> bool: ...
    @overload
    def isMapEmpty() -> bool: ...
    @property
    def KF_options(self) -> Any: ...

class CKalmanFilterCapable_7UL_3UL_3UL_7UL_double_t:
    def __init__(self, *args, **kwargs) -> None: ...
    def OnNewLandmarkAddedToMap(self, in_obsIdx: int, in_idxNewFeat: int) -> None: ...
    @overload
    def OnNormalizeStateVector(self) -> None: ...
    @overload
    def OnNormalizeStateVector() -> void: ...
    @overload
    def OnPostIteration(self) -> None: ...
    @overload
    def OnPostIteration() -> void: ...
    def getLandmarkCov(self, idx: int, feat_cov: mrpt.pymrpt.mrpt.math.CMatrixFixed_double_3UL_3UL_t) -> None: ...
    def getLandmarkMean(self, idx: int, feat: mrpt.pymrpt.mrpt.math.CMatrixFixed_double_3UL_1UL_t) -> None: ...
    @overload
    def getNumberOfLandmarksInTheMap(self) -> int: ...
    @overload
    def getNumberOfLandmarksInTheMap() -> size_t: ...
    def getProfiler(self) -> mrpt.pymrpt.mrpt.system.CTimeLogger: ...
    @overload
    def getStateVectorLength(self) -> int: ...
    @overload
    def getStateVectorLength() -> size_t: ...
    def get_action_size(self, *args, **kwargs) -> Any: ...
    def get_feature_size(self, *args, **kwargs) -> Any: ...
    def get_observation_size(self, *args, **kwargs) -> Any: ...
    def get_vehicle_size(self, *args, **kwargs) -> Any: ...
    def internal_getPkk(self) -> mrpt.pymrpt.mrpt.math.CMatrixDynamic_double_t: ...
    def internal_getXkk(self, *args, **kwargs) -> Any: ...
    @overload
    def isMapEmpty(self) -> bool: ...
    @overload
    def isMapEmpty() -> bool: ...
    @property
    def KF_options(self) -> Any: ...

class CParticleFilter:
    class TParticleFilterAlgorithm:
        __doc__: ClassVar[str] = ...  # read-only
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        pfAuxiliaryPFOptimal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
        pfAuxiliaryPFStandard: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
        pfOptimalProposal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
        pfStandardProposal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
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

    class TParticleFilterOptions(mrpt.pymrpt.mrpt.config.CLoadableOptions):
        BETA: float
        PF_algorithm: CParticleFilter.TParticleFilterAlgorithm
        adaptiveSampleSize: bool
        max_loglikelihood_dyn_range: float
        pfAuxFilterOptimal_MLE: bool
        pfAuxFilterOptimal_MaximumSearchSamples: int
        pfAuxFilterStandard_FirstStageWeightsMonteCarlo: bool
        powFactor: float
        resamplingMethod: CParticleFilter.TParticleResamplingAlgorithm
        sampleSize: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: CParticleFilter.TParticleFilterOptions) -> None: ...
        @overload
        def __init__(self, arg0: CParticleFilter.TParticleFilterOptions) -> None: ...
        def assign(self) -> CParticleFilter.TParticleFilterOptions: ...
        @overload
        def loadFromConfigFile(self, source, section: str) -> None: ...
        @overload
        def loadFromConfigFile(constclassmrpt, conststd) -> void: ...
        @overload
        def saveToConfigFile(self, target, section: str) -> None: ...
        @overload
        def saveToConfigFile(classmrpt, conststd) -> void: ...

    class TParticleFilterStats:
        ESS_beforeResample: float
        weightsVariance_beforeResample: float
        def __init__(self) -> None: ...

    class TParticleResamplingAlgorithm:
        __doc__: ClassVar[str] = ...  # read-only
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        prMultinomial: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
        prResidual: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
        prStratified: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
        prSystematic: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
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
    pfAuxiliaryPFOptimal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
    pfAuxiliaryPFStandard: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
    pfOptimalProposal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
    pfStandardProposal: ClassVar[CParticleFilter.TParticleFilterAlgorithm] = ...
    prMultinomial: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
    prResidual: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
    prStratified: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
    prSystematic: ClassVar[CParticleFilter.TParticleResamplingAlgorithm] = ...
    m_options: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilter) -> None: ...
    def assign(self) -> CParticleFilter: ...
    @overload
    def executeOn(self, obj, action, observation) -> None: ...
    @overload
    def executeOn(self, obj, action, observation, stats) -> None: ...

class CParticleFilterCapable:
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS(EstimatedSampleSize) -> Any: ...
    @overload
    def ESS() -> double: ...
    def assign(self) -> CParticleFilterCapable: ...
    def defaultEvaluator(self, *args, **kwargs) -> Any: ...
    def fastDrawSample(self, *args, **kwargs) -> Any: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions) -> None: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions, out_particle_count: int) -> None: ...
    @overload
    def performResampling(conststructmrpt, size_t) -> void: ...
    def prediction_and_update(self, *args, **kwargs) -> Any: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...

class CParticleFilterDataImpl_mrpt_maps_CMultiMetricMapPDF_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t(CParticleFilterCapable):
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_maps_CMultiMetricMapPDF_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_maps_CMultiMetricMapPDF_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS() -> double: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS(EstimatedSampleSize) -> Any: ...
    @overload
    def ESS() -> double: ...
    @overload
    def assign(self) -> CParticleFilterDataImpl_mrpt_maps_CMultiMetricMapPDF_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t: ...
    @overload
    def assign(self) -> CParticleFilterCapable: ...
    def defaultEvaluator(self, *args, **kwargs) -> Any: ...
    def derived(self, *args, **kwargs) -> Any: ...
    def fastDrawSample(self, *args, **kwargs) -> Any: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions) -> None: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions, out_particle_count: int) -> None: ...
    @overload
    def performResampling(conststructmrpt, size_t) -> void: ...
    def prediction_and_update(self, *args, **kwargs) -> Any: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...

class CParticleFilterDataImpl_mrpt_poses_CPointPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t(CParticleFilterCapable):
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPointPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPointPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS() -> double: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS(EstimatedSampleSize) -> Any: ...
    @overload
    def ESS() -> double: ...
    @overload
    def assign(self) -> CParticleFilterDataImpl_mrpt_poses_CPointPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t: ...
    @overload
    def assign(self) -> CParticleFilterCapable: ...
    def defaultEvaluator(self, *args, **kwargs) -> Any: ...
    def derived(self, *args, **kwargs) -> Any: ...
    def fastDrawSample(self, *args, **kwargs) -> Any: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions) -> None: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions, out_particle_count: int) -> None: ...
    @overload
    def performResampling(conststructmrpt, size_t) -> void: ...
    def prediction_and_update(self, *args, **kwargs) -> Any: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...

class CParticleFilterDataImpl_mrpt_poses_CPose3DPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t(CParticleFilterCapable):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPose3DPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPose3DPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS() -> double: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS(EstimatedSampleSize) -> Any: ...
    @overload
    def ESS() -> double: ...
    @overload
    def assign(self) -> CParticleFilterDataImpl_mrpt_poses_CPose3DPDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t: ...
    @overload
    def assign(self) -> CParticleFilterCapable: ...
    def defaultEvaluator(self, *args, **kwargs) -> Any: ...
    def derived(self, *args, **kwargs) -> Any: ...
    def fastDrawSample(self, *args, **kwargs) -> Any: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions) -> None: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions, out_particle_count: int) -> None: ...
    @overload
    def performResampling(conststructmrpt, size_t) -> void: ...
    def prediction_and_update(self, *args, **kwargs) -> Any: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...

class CParticleFilterDataImpl_mrpt_poses_CPosePDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t(CParticleFilterCapable):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPosePDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterDataImpl_mrpt_poses_CPosePDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS() -> double: ...
    @overload
    def ESS(self) -> float: ...
    @overload
    def ESS(EstimatedSampleSize) -> Any: ...
    @overload
    def ESS() -> double: ...
    @overload
    def assign(self) -> CParticleFilterDataImpl_mrpt_poses_CPosePDFParticles_std_deque_mrpt_bayes_CProbabilityParticle_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t: ...
    @overload
    def assign(self) -> CParticleFilterCapable: ...
    def defaultEvaluator(self, *args, **kwargs) -> Any: ...
    def derived(self, *args, **kwargs) -> Any: ...
    def fastDrawSample(self, *args, **kwargs) -> Any: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def getW(self, i: int) -> float: ...
    @overload
    def getW(size_t) -> double: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def normalizeWeights(self) -> float: ...
    @overload
    def normalizeWeights(self, out_max_log_w: float) -> float: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def particlesCount(self) -> int: ...
    @overload
    def particlesCount() -> size_t: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions) -> None: ...
    @overload
    def performResampling(self, PF_options: CParticleFilter.TParticleFilterOptions, out_particle_count: int) -> None: ...
    @overload
    def performResampling(conststructmrpt, size_t) -> void: ...
    def prediction_and_update(self, *args, **kwargs) -> Any: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...
    @overload
    def setW(self, i: int, w: float) -> None: ...
    @overload
    def setW(size_t, double) -> void: ...

class CParticleFilterData_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t:
    m_particles: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterData_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    def assign(self) -> CParticleFilterData_mrpt_maps_CRBPFParticleData_mrpt_bayes_particle_storage_mode_POINTER_t: ...
    @overload
    def clearParticles(self) -> None: ...
    @overload
    def clearParticles() -> void: ...

class CParticleFilterData_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t:
    m_particles: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterData_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    def assign(self) -> CParticleFilterData_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t: ...
    @overload
    def clearParticles(self) -> None: ...
    @overload
    def clearParticles() -> void: ...
    def getMostLikelyParticle(self, *args, **kwargs) -> Any: ...

class CParticleFilterData_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t:
    m_particles: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterData_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    def assign(self) -> CParticleFilterData_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t: ...
    @overload
    def clearParticles(self) -> None: ...
    @overload
    def clearParticles() -> void: ...
    def getMostLikelyParticle(self, *args, **kwargs) -> Any: ...

class CParticleFilterData_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t:
    m_particles: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CParticleFilterData_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t) -> None: ...
    def assign(self) -> CParticleFilterData_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t: ...
    @overload
    def clearParticles(self) -> None: ...
    @overload
    def clearParticles() -> void: ...
    def getMostLikelyParticle(self, *args, **kwargs) -> Any: ...

class CProbabilityParticleBase:
    log_w: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, logw: float) -> None: ...
    @overload
    def __init__(self, arg0: CProbabilityParticleBase) -> None: ...
    def assign(self) -> CProbabilityParticleBase: ...

class CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t(CProbabilityParticleBase):
    d: Any
    log_w: float
    @overload
    def __init__(self, arg0: CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def assign(self) -> CProbabilityParticle_mrpt_math_TPoint3D_float_mrpt_bayes_particle_storage_mode_POINTER_t: ...
    @overload
    def assign(self) -> CProbabilityParticleBase: ...

class CProbabilityParticle_mrpt_math_TPose2D_mrpt_bayes_particle_storage_mode_VALUE_t(CProbabilityParticleBase):
    d: mrpt.pymrpt.mrpt.math.TPose2D
    log_w: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, data: mrpt.pymrpt.mrpt.math.TPose2D, logw: float) -> None: ...
    def assign(self) -> CProbabilityParticleBase: ...

class CProbabilityParticle_mrpt_math_TPose3D_mrpt_bayes_particle_storage_mode_VALUE_t(CProbabilityParticleBase):
    d: mrpt.pymrpt.mrpt.math.TPose3D
    log_w: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, data: mrpt.pymrpt.mrpt.math.TPose3D, logw: float) -> None: ...
    def assign(self) -> CProbabilityParticleBase: ...

class CRejectionSamplingCapable_mrpt_poses_CPose2D_mrpt_bayes_particle_storage_mode_POINTER_t:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CRejectionSamplingCapable_mrpt_poses_CPose2D_mrpt_bayes_particle_storage_mode_POINTER_t) -> None: ...
    def assign(self) -> CRejectionSamplingCapable_mrpt_poses_CPose2D_mrpt_bayes_particle_storage_mode_POINTER_t: ...

class TKFMethod:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    kfEKFAlaDavison: ClassVar[TKFMethod] = ...
    kfEKFNaive: ClassVar[TKFMethod] = ...
    kfIKF: ClassVar[TKFMethod] = ...
    kfIKFFull: ClassVar[TKFMethod] = ...
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

class TKF_options(mrpt.pymrpt.mrpt.config.CLoadableOptions):
    IKF_iterations: int
    debug_verify_analytic_jacobians: bool
    debug_verify_analytic_jacobians_threshold: float
    enable_profiler: bool
    method: TKFMethod
    use_analytic_observation_jacobian: bool
    use_analytic_transition_jacobian: bool
    @overload
    def __init__(self, verb_level_ref: mrpt.pymrpt.mrpt.system.VerbosityLevel) -> None: ...
    @overload
    def __init__(self, arg0: TKF_options) -> None: ...
    @overload
    def __init__(self, arg0: TKF_options) -> None: ...
    @overload
    def loadFromConfigFile(self, iniFile: mrpt.pymrpt.mrpt.config.CConfigFileBase, section: str) -> None: ...
    @overload
    def loadFromConfigFile(constclassmrpt, conststd) -> void: ...

class particle_storage_mode:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    POINTER: ClassVar[particle_storage_mode] = ...
    VALUE: ClassVar[particle_storage_mode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...