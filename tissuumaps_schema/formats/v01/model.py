from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field

from ..model import Project as ProjectBase


class ColorScale(str, Enum):
    INTERPOLATE_CUBEHELIX_DEFAULT = "interpolateCubehelixDefault"
    INTERPOLATE_RAINBOW = "interpolateRainbow"
    INTERPOLATE_WARM = "interpolateWarm"
    INTERPOLATE_COOL = "interpolateCool"
    INTERPOLATE_VIRIDIS = "interpolateViridis"
    INTERPOLATE_MAGMA = "interpolateMagma"
    INTERPOLATE_INFERNO = "interpolateInferno"
    INTERPOLATE_PLASMA = "interpolatePlasma"
    INTERPOLATE_BLUES = "interpolateBlues"
    INTERPOLATE_BR_BG = "interpolateBrBG"
    INTERPOLATE_BU_GN = "interpolateBuGn"
    INTERPOLATE_BU_PU = "interpolateBuPu"
    INTERPOLATE_CIVIDIS = "interpolateCividis"
    INTERPOLATE_GN_BU = "interpolateGnBu"
    INTERPOLATE_GREENS = "interpolateGreens"
    INTERPOLATE_GREYS = "interpolateGreys"
    INTERPOLATE_OR_RD = "interpolateOrRd"
    INTERPOLATE_ORANGES = "interpolateOranges"
    INTERPOLATE_PR_GN = "interpolatePRGn"
    INTERPOLATE_PI_YG = "interpolatePiYG"
    INTERPOLATE_PU_BU = "interpolatePuBu"
    INTERPOLATE_PU_BU_GN = "interpolatePuBuGn"
    INTERPOLATE_PU_OR = "interpolatePuOr"
    INTERPOLATE_PU_RD = "interpolatePuRd"
    INTERPOLATE_PURPLES = "interpolatePurples"
    INTERPOLATE_RD_BU = "interpolateRdBu"
    INTERPOLATE_RD_GY = "interpolateRdGy"
    INTERPOLATE_RD_PU = "interpolateRdPu"
    INTERPOLATE_RD_YL_BU = "interpolateRdYlBu"
    INTERPOLATE_RD_YL_GN = "interpolateRdYlGn"
    INTERPOLATE_REDS = "interpolateReds"
    INTERPOLATE_SINEBOW = "interpolateSinebow"
    INTERPOLATE_SPECTRAL = "interpolateSpectral"
    INTERPOLATE_TURBO = "interpolateTurbo"
    INTERPOLATE_YL_GN = "interpolateYlGn"
    INTERPOLATE_YL_GN_BU = "interpolateYlGnBu"
    INTERPOLATE_YL_OR_BR = "interpolateYlOrBr"
    INTERPOLATE_YL_OR_RD = "interpolateYlOrRd"


class CompositeMode(str, Enum):
    SOURCE_OVER = "source-over"
    LIGHTER = "lighter"


class Filter(str, Enum):
    COLOR = "Color"
    BRIGHTNESS = "Brightness"
    EXPOSURE = "Exposure"
    HUE = "Hue"
    CONTRAST = "Contrast"
    VIBRANCE = "Vibrance"
    NOISE = "Noise"
    SATURATION = "Saturation"
    GAMMA = "Gamma"
    INVERT = "Invert"
    GREYSCALE = "Greyscale"
    THRESHOLD = "Threshold"
    EROSION = "Erosion"
    DILATION = "Dilation"


class Shape(str, Enum):
    CROSS = "cross"
    DIAMOND = "diamond"
    SQUARE = "square"
    TRIANGLE_UP = "triangle up"
    STAR = "star"
    CLOBBER = "clobber"
    DISC = "disc"
    HBAR = "hbar"
    VBAR = "vbar"
    TAILED_ARROW = "tailed arrow"
    TRIANGLE_DOWN = "triangle down"
    RING = "ring"
    X = "x"
    ARROW = "arrow"


class Layer(BaseModel):
    name: str
    tile_source: str = Field(alias="tileSource")


class LayerFilter(BaseModel):
    name: Filter
    value: str


class BoundingBox(BaseModel):
    x: float
    y: float
    width: float
    height: float


class Setting(BaseModel):
    module: str
    function: str
    value: Union[int, float]


class ExpectedHeader(BaseModel):
    x: str = Field(alias="X")
    y: str = Field(alias="Y")
    gb_col: Optional[str] = None
    gb_name: Optional[str] = None
    cb_cmap: str = ""
    cb_col: Optional[str] = None
    cb_gr_dict: str = ""
    scale_col: Optional[str] = None
    scale_factor: str = "1"
    pie_col: Optional[str] = None
    pie_dict: str = ""
    shape_col: Optional[str] = None
    shape_fixed: str = "cross"
    shape_gr_dict: str = ""
    opacity_col: Optional[str] = None
    opacity: str = "1"
    tooltip_fmt: str = ""


class ExpectedRadios(BaseModel):
    cb_col: bool = False
    cb_gr: bool = True
    cb_gr_rand: bool = False
    cb_gr_dict: bool = False
    cb_gr_key: bool = True
    pie_check: bool = False
    scale_check: bool = False
    shape_col: bool = False
    shape_gr: bool = True
    shape_gr_rand: bool = True
    shape_gr_dict: bool = False
    shape_fixed: bool = False
    opacity_check: bool = False
    no_outline: bool = Field(default=False, alias="_no_outline")


class MarkerFile(BaseModel):
    title: str
    comment: str = ""
    name: str
    auto_load: bool = Field(default=False, alias="autoLoad")
    hide_settings: bool = Field(default=False, alias="hideSettings")
    uid: str
    expected_header: ExpectedHeader = Field(alias="expectedHeader")
    expected_radios: ExpectedRadios = Field(
        default_factory=lambda: ExpectedRadios(), alias="expectedRadios"
    )
    path: Union[str, list[str]]
    settings: list[Setting] = []


class RegionFile(BaseModel):
    title: str
    comment: str = ""
    auto_load: bool = Field(default=False, alias="autoLoad")
    path: Union[str, list[str]]
    settings: list[Setting] = []


class Project(ProjectBase):
    version: str = "0.1"
    filename: str
    layers: list[Layer] = []
    layer_opacities: dict[str, int] = Field(default={}, alias="layerOpacities")
    layer_visibilities: dict[str, bool] = Field(default={}, alias="layerVisibilities")
    layer_filters: dict[str, LayerFilter] = Field(default={}, alias="layerFilters")
    filters: list[Filter] = [Filter.SATURATION, Filter.BRIGHTNESS, Filter.CONTRAST]
    composite_mode: CompositeMode = Field(
        default=CompositeMode.SOURCE_OVER, alias="compositeMode"
    )
    mpp: Optional[float] = None
    bounding_box: Optional[BoundingBox] = Field(default=None, alias="boundingBox")
    rotate: int = 0
    marker_files: list[MarkerFile] = Field(default=[], alias="markerFiles")
    regions: list[Any] = []
    region_files: list[RegionFile] = Field(default=[], alias="regionFiles")
    plugins: list[str] = []
    hide_tabs: bool = Field(default=False, alias="hideTabs")
    settings: list[Setting] = []
