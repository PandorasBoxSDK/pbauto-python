import socket
import struct

# Pandoras Box Automation
# pbauto-python v0.6.12086 @2016-06-18 <support@coolux.de>


class ParamKind:
    No = 0
    Opacity = 1
    Mesh = 2
    Media = 3
    Inpoint = 4
    Outpoint = 5
    Transport = 6
    XPos = 8
    YPos = 9
    ZPos = 10
    XAngle = 11
    YAngle = 12
    ZAngle = 13
    XScale = 14
    YScale = 15
    ZScale = 16
    XAxis = 25
    YAxis = 26
    ZAxis = 27
    XOffset = 29
    YOffset = 30
    KSL = 32
    Kslr = 33
    Ksr = 34
    Ksrr = 35
    Kst = 36
    Kstr = 37
    Ksb = 38
    Ksbr = 39
    LinX = 40
    LinY = 41
    Sel = 42
    Selc = 43
    Ser = 44
    Serc = 45
    Set = 46
    Setc = 47
    Seb = 48
    Sebc = 49
    Volume = 50
    X = 51
    Z = 52
    RoomSize = 53
    Ambience = 54
    Diffusion = 55
    BlendMode = 56
    FxHue = 57
    FxSaturation = 58
    FxBrightness = 59
    MultiFxList = 60
    VideoSpeed = 61
    AudioPan = 62
    RotPivotXPos = 63
    RotPivotYPos = 64
    RotPivotZPos = 65
    ScalePivotXPos = 66
    ScalePivotYPos = 67
    ScalePivotZPos = 68
    XRotSpeed = 69
    YRotSpeed = 70
    ZRotSpeed = 71
    CamTargetXPos = 72
    CamTargetYPos = 73
    CamTargetZPos = 74
    CamFov = 75
    CamNearPlane = 76
    CamFarPlane = 77
    CamAspect = 78
    CamZRoll = 79
    CamPostBypass = 80
    CamProjMode = 81
    ParticleGravity = 82
    ParticleSpawnRate = 83
    ParticleSpeed = 84
    ParticleTimeToLive = 85
    ParticleWind = 86
    ParticleWindPosX = 87
    ParticleWindPosY = 88
    ParticleWindPosZ = 89
    ParticleWindRotX = 90
    ParticleWindRotY = 91
    ParticleWindRotZ = 92
    ParticleEmitterType = 93
    ParticleEmitterRadius = 94
    ParticleEmitterRadiusOption = 95
    ParticleMass = 96
    ParticleEmissionAngle = 97
    ParticleAlignment = 98
    ParticleDrag = 99
    ParticleEmissionRange = 100
    CamState = 101
    AudioVolume = 102
    ParticleColor = 103
    ParticleOpacity = 104
    Selm = 105
    Selmw = 106
    Serm = 107
    Sermw = 108
    Setm = 109
    Setmw = 110
    Sebm = 111
    Sebmw = 112
    ParticleXScale = 113
    ParticleYScale = 114
    ParticleZScale = 115
    PsOpacity = 116
    ParticleRotationX = 117
    ParticleRotationY = 118
    ParticleRotationZ = 119
    XRotMode = 120
    YRotMode = 121
    ZRotMode = 122
    LightXPos = 123
    LightYPos = 124
    LightZPos = 125
    LightTargetXPos = 126
    LightTargetYPos = 127
    LightTargetZPos = 128
    LightAngle = 129
    LightMedia = 130
    LightIntensity = 131
    LightColorRed = 132
    LightColorGreen = 133
    LightColorBlue = 134
    LightAspect = 135
    LightZRoll = 136
    LightTolerance = 137
    ShadowSoftness = 138
    WidgetValue1 = 140
    WidgetValue2 = 141
    WidgetValue3 = 142
    WidgetValue4 = 143
    WidgetValue5 = 144
    WidgetValue6 = 145
    WidgetValue7 = 146
    WidgetValue8 = 147
    WidgetValue9 = 148
    WidgetValue10 = 149
    WidgetValue11 = 150
    WidgetValue12 = 151
    MatrixMix = 152
    MatrixTexture = 153
    MatrixPatch = 154
    PointerLoopInPoint = 155
    PointerOutDelay = 156
    PointerOffsetX = 157
    PointerOffsetY = 158
    RtClearColorRed = 159
    RtClearColorGreen = 160
    RtClearColorBlue = 161
    RtClearColorAlpha = 162
    GenPerspTargetPt1X = 163
    GenPerspTargetPt1Y = 164
    GenPerspTargetPt1Z = 165
    GenPerspTargetPt2X = 166
    GenPerspTargetPt2Y = 167
    GenPerspTargetPt2Z = 168
    GenPerspTargetPt3X = 169
    GenPerspTargetPt3Y = 170
    GenPerspTargetPt3Z = 171
    EngineGlobalParam = 172
    BrowserUrl = 173
    CameraPre = 174
    LightProjMode = 175
    DefaultMeshShadingWireRed = 176
    DefaultMeshShadingWireGreen = 177
    DefaultMeshShadingWireBlue = 178
    DefaultMeshShadingWireAlpha = 179
    DefaultMeshShadingFillRed = 180
    DefaultMeshShadingFillGreen = 181
    DefaultMeshShadingFillBlue = 182
    DefaultMeshShadingFillAlpha = 183
    DefaultMeshShadingWireWidth = 184
    DefaultMeshShadingAmbient = 185
    DefaultMeshShadingDiffuse = 186
    DefaultMeshShadingSpecular = 187
    DefaultMeshShadingShininess = 188
    DefaultMeshShadingWireBrightnessFactor = 189

class ClxHardware:
    FaderExtension = 0
    JogShuttle = 1

class Consistency:
    Inconsistent = 1
    Consistent = 0

class SelectionMode:
    SetSelection = 0
    AddSelection = 1
    Unselect = 2
    UnselectAll = 3

class WatchFolderProperty:
    IncludeSubdirectories = 1
    DeleteInProject = 2
    DeleteInClients = 3

class TransportMode:
    Play = 1
    Pause = 3
    Stop = 2

class SequenceSmpteMode:
    No = 0
    Send = 1
    Receive = 2

class SequenceSmpteStopMode:
    No = 0
    Stop = 1
    Pause = 2
    Continue = 3

class MediaOption:
    AnisotropicFiltering = 1
    IgnoreThumbnail = 2
    VideoAlphaChannel = 4
    FluidFrame = 8
    OptimizeMpegColorspace = 16
    Underscan = 32
    OptimizeLooping = 64
    MuteSound = 128


class PBAuto:
    @staticmethod
    def connect_tcp(ip="", domain=0):
        return PBAuto(Tcp(ip, domain))

    @staticmethod
    def offline_tcp(domain=0, callback=print, data_format='hex'):
        return PBAuto(OfflineTcp(domain, callback, data_format))

    def __init__(self, connector):
        if not issubclass(type(connector), Connector):
            raise TypeError('Expected Connector')
        self.__c = connector

    def set_param_int(self, site_id, device_id, parameter_name, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(1)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_int(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_double(self, site_id, device_id, parameter_name, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(84)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_double(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_byte_tuples(self, site_id, device_id, parameter_name, tuple_dimension, tuple_data, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(115)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_int(tuple_dimension)
        b.write_byte_buffer(tuple_data)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def get_param(self, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(79)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['parameterValue'] = r.read_double()
        return d

    def get_param_byte_tuples(self, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(132)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_wide(parameter_name)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['tupleDimension'] = r.read_int()
        d['tupleData'] = r.read_byte_buffer()
        return d

    def set_param_of_kind(self, site_id, device_id, parameter_kind_id, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(39)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(parameter_kind_id)
        b.write_int(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_of_kind_double(self, site_id, device_id, parameter_kind_id, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(85)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(parameter_kind_id)
        b.write_double(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def get_param_of_kind(self, site_id, device_id, parameter_kind_id):
        b = ByteUtil()
        b.write_short(80)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(parameter_kind_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['parameterValue'] = r.read_double()
        return d

    def set_param_in_selection(self, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(58)
        b.write_string_narrow(parameter_name)
        b.write_int(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_in_selection_double(self, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(99)
        b.write_string_narrow(parameter_name)
        b.write_double(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_of_kind_in_selection(self, parameter_kind_id, parameter_value):
        b = ByteUtil()
        b.write_short(59)
        b.write_int(parameter_kind_id)
        b.write_int(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_of_kind_in_selection_double(self, parameter_kind_id, parameter_value):
        b = ByteUtil()
        b.write_short(100)
        b.write_int(parameter_kind_id)
        b.write_double(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_lerp_time(self, site_id, device_id, parameter_name, smoothing_time):
        b = ByteUtil()
        b.write_short(232)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_int(smoothing_time)
        self.__c.send(b, False)
        return {'ok': True}

    def get_is_device_selected(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(74)
        b.write_int(site_id)
        b.write_int(device_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isSelected'] = r.read_byte()
        return d

    def get_selected_device_count(self):
        b = ByteUtil()
        b.write_short(81)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['selectedDevicesCount'] = r.read_int()
        return d

    def get_selected_device(self, selection_index):
        b = ByteUtil()
        b.write_short(75)
        b.write_int(selection_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['siteId'] = r.read_int()
        d['deviceId'] = r.read_int()
        return d

    def set_sequence_media_at_time(self, site_id, device_id, sequence_id, hours, minutes, seconds, frames, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(56)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(sequence_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource(self, site_id, device_id, dmx_folder_id, dmx_file_id, for_mesh):
        b = ByteUtil()
        b.write_short(2)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(for_mesh)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource_by_name(self, site_id, device_id, resource_path, parameter_name, for_mesh):
        b = ByteUtil()
        b.write_short(129)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_wide(resource_path)
        b.write_string_wide(parameter_name)
        b.write_bool(for_mesh)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource_to_selection(self, dmx_folder_id, dmx_file_id, for_mesh):
        b = ByteUtil()
        b.write_short(61)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(for_mesh)
        self.__c.send(b, False)
        return {'ok': True}

    def move_resource_to_path(self, resource_path, project_path):
        b = ByteUtil()
        b.write_short(144)
        b.write_string_wide(resource_path)
        b.write_string_wide(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def move_tree_item(self, item_id_from, item_id_to):
        b = ByteUtil()
        b.write_short(158)
        b.write_int(item_id_from)
        b.write_int(item_id_to)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_transport_mode(self, sequence_id, transport_mode):
        b = ByteUtil()
        b.write_short(3)
        b.write_int(sequence_id)
        b.write_int(transport_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def get_sequence_transport_mode(self, sequence_id):
        b = ByteUtil()
        b.write_short(72)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['transportMode'] = r.read_int()
        return d

    def move_sequence_to_time(self, sequence_id, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(5)
        b.write_int(sequence_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def get_sequence_time(self, sequence_id):
        b = ByteUtil()
        b.write_short(73)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        return d

    def move_sequence_to_next_frame(self, sequence_id, is_next):
        b = ByteUtil()
        b.write_short(6)
        b.write_int(sequence_id)
        b.write_byte(is_next)
        self.__c.send(b, False)
        return {'ok': True}

    def move_sequence_to_cue(self, sequence_id, cue_id):
        b = ByteUtil()
        b.write_short(4)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        self.__c.send(b, False)
        return {'ok': True}

    def move_sequence_to_next_cue(self, sequence_id, is_next):
        b = ByteUtil()
        b.write_short(7)
        b.write_int(sequence_id)
        b.write_byte(is_next)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_transparency(self, sequence_id, transparency):
        b = ByteUtil()
        b.write_short(8)
        b.write_int(sequence_id)
        b.write_int(transparency)
        self.__c.send(b, False)
        return {'ok': True}

    def get_sequence_transparency(self, sequence_id):
        b = ByteUtil()
        b.write_short(91)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['transparency'] = r.read_int()
        return d

    def set_sequence_smtpe_time_code_mode(self, sequence_id, time_code_mode):
        b = ByteUtil()
        b.write_short(41)
        b.write_int(sequence_id)
        b.write_int(time_code_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_smtpe_time_code_offset(self, sequence_id, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(42)
        b.write_int(sequence_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_smtpe_time_code_stop_action(self, sequence_id, stop_action):
        b = ByteUtil()
        b.write_short(43)
        b.write_int(sequence_id)
        b.write_int(stop_action)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_all(self):
        b = ByteUtil()
        b.write_short(9)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_site(self, site_id):
        b = ByteUtil()
        b.write_short(10)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_device(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(11)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_param(self, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(12)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_all_active(self):
        b = ByteUtil()
        b.write_short(35)
        self.__c.send(b, False)
        return {'ok': True}

    def set_site_active(self, site_id):
        b = ByteUtil()
        b.write_short(36)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_device_active(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(37)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_active(self, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(38)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_all_active(self):
        b = ByteUtil()
        b.write_short(13)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_active_site(self, site_id):
        b = ByteUtil()
        b.write_short(14)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_active_device(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(15)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_active_param(self, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(16)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def toggle_fullscreen(self, site_id):
        b = ByteUtil()
        b.write_short(17)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_relative_double(self, site_id, device_id, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(98)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_double(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_relative_extended(self, site_id, device_id, parameter_name, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(149)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_double(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_relative_in_selection(self, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(60)
        b.write_string_narrow(parameter_name)
        b.write_int(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_relative_in_selection_double(self, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(101)
        b.write_string_narrow(parameter_name)
        b.write_double(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_to_path(self, file_path, site_id, dmx_folder_id, dmx_file_id, project_path):
        b = ByteUtil()
        b.write_short(87)
        b.write_string_narrow(file_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_to_tree_item(self, file_path, site_id, dmx_folder_id, dmx_file_id, tree_item_index):
        b = ByteUtil()
        b.write_short(153)
        b.write_string_narrow(file_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_local_node(self, file_path, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(63)
        b.write_string_narrow(file_path)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_local_node_to_path(self, file_path, project_path, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(135)
        b.write_string_narrow(file_path)
        b.write_string_narrow(project_path)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_local_node_to_tree_item(self, file_path, tree_item_index, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(154)
        b.write_string_narrow(file_path)
        b.write_int(tree_item_index)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_folder(self, folder_path, site_id, dmx_folder_id, dmx_file_id, project_path):
        b = ByteUtil()
        b.write_short(124)
        b.write_string_wide(folder_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_wide(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_local_node_folder(self, folder_path, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(133)
        b.write_string_wide(folder_path)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_from_local_node_folder_to_path(self, folder_path, project_path, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(134)
        b.write_string_narrow(folder_path)
        b.write_string_narrow(project_path)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content_folder_from_local_node_to_tree_item(self, folder_path, tree_item_index, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(155)
        b.write_string_narrow(folder_path)
        b.write_int(tree_item_index)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_media_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(20)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_mesh_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(21)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_content_by_name(self, resource_path, all_equally_named):
        b = ByteUtil()
        b.write_short(125)
        b.write_string_wide(resource_path)
        b.write_bool(all_equally_named)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_tree_item(self, tree_item_index):
        b = ByteUtil()
        b.write_short(156)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_all_resources(self, remove_folder):
        b = ByteUtil()
        b.write_short(126)
        b.write_bool(remove_folder)
        self.__c.send(b, False)
        return {'ok': True}

    def set_content_id(self, resource_path, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(234)
        b.write_string_wide(resource_path)
        b.write_short(dmx_folder_id)
        b.write_short(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def spread_all(self):
        b = ByteUtil()
        b.write_short(22)
        self.__c.send(b, False)
        return {'ok': True}

    def spread_media_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(23)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def spread_mesh_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(24)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_media_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(44)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_mesh_by_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(45)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_resource(self, resource_path):
        b = ByteUtil()
        b.write_short(147)
        b.write_string_wide(resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def spread_resource(self, resource_path):
        b = ByteUtil()
        b.write_short(148)
        b.write_string_wide(resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_and_spread_resource_by_path(self, resource_path):
        b = ByteUtil()
        b.write_short(159)
        b.write_string_wide(resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_and_spread_resource_by_tree_item(self, tree_item_index):
        b = ByteUtil()
        b.write_short(160)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def reload_and_spread_resource_by_dmx_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(161)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_inconsistent(self):
        b = ByteUtil()
        b.write_short(34)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_asset_on_site(self, resource_path, site_id):
        b = ByteUtil()
        b.write_short(170)
        b.write_string_wide(resource_path)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_asset_on_site_by_id(self, dmx_folder_id, dmx_file_id, site_id):
        b = ByteUtil()
        b.write_short(171)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_asset_on_site_by_tree_item(self, tree_item_index, site_id):
        b = ByteUtil()
        b.write_short(172)
        b.write_int(tree_item_index)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def attach_asset_on_site(self, file_path, resource_path, site_id):
        b = ByteUtil()
        b.write_short(173)
        b.write_string_wide(file_path)
        b.write_string_wide(resource_path)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def attach_asset_on_site_by_dmx_id(self, file_path, dmx_folder_id, dmx_file_id, site_id):
        b = ByteUtil()
        b.write_short(174)
        b.write_string_wide(file_path)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def attach_asset_on_site_by_tree_item(self, file_path, tree_item_index, site_id):
        b = ByteUtil()
        b.write_short(175)
        b.write_string_wide(file_path)
        b.write_int(tree_item_index)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def store_active(self, sequence_id):
        b = ByteUtil()
        b.write_short(25)
        b.write_int(sequence_id)
        self.__c.send(b, False)
        return {'ok': True}

    def store_active_to_time(self, sequence_id, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(26)
        b.write_int(sequence_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_frame_blending_by_id(self, dmx_folder_id, dmx_file_id, frame_blended):
        b = ByteUtil()
        b.write_short(27)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(frame_blended)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_deinterlacing_by_id(self, dmx_folder_id, dmx_file_id, deinterlacer):
        b = ByteUtil()
        b.write_short(28)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(deinterlacer)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_anisotropic_filtering_by_id(self, dmx_folder_id, dmx_file_id, use_filtering):
        b = ByteUtil()
        b.write_short(29)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(use_filtering)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_underscan_by_id(self, dmx_folder_id, dmx_file_id, use_underscan):
        b = ByteUtil()
        b.write_short(30)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(use_underscan)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_mpeg_colour_space_by_id(self, dmx_folder_id, dmx_file_id, use_mpeg_color_space):
        b = ByteUtil()
        b.write_short(31)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(use_mpeg_color_space)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_alpha_channel_by_id(self, dmx_folder_id, dmx_file_id, use_alpha_channel):
        b = ByteUtil()
        b.write_short(32)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(use_alpha_channel)
        self.__c.send(b, False)
        return {'ok': True}

    def create_text_input(self, dmx_folder_id, dmx_file_id, text):
        b = ByteUtil()
        b.write_short(52)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(text)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text(self, dmx_folder_id, dmx_file_id, text):
        b = ByteUtil()
        b.write_short(33)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(text)
        self.__c.send(b, False)
        return {'ok': True}

    def load_project(self, folder_path_to_project, project_xml_file_name, save_existing):
        b = ByteUtil()
        b.write_short(46)
        b.write_string_narrow(folder_path_to_project)
        b.write_string_narrow(project_xml_file_name)
        b.write_byte(save_existing)
        self.__c.send(b, False)
        return {'ok': True}

    def close_project(self, save):
        b = ByteUtil()
        b.write_short(47)
        b.write_byte(save)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_selection(self):
        b = ByteUtil()
        b.write_short(48)
        self.__c.send(b, False)
        return {'ok': True}

    def set_device_accept_dmx_by_id(self, site_id, device_id, accept_dmx):
        b = ByteUtil()
        b.write_short(49)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_byte(accept_dmx)
        self.__c.send(b, False)
        return {'ok': True}

    def set_site_accept_dmx_by_id(self, site_id, accept_dmx):
        b = ByteUtil()
        b.write_short(50)
        b.write_int(site_id)
        b.write_byte(accept_dmx)
        self.__c.send(b, False)
        return {'ok': True}

    def set_device_dmx_address_by_id(self, site_id, device_id, index, id1, id2):
        b = ByteUtil()
        b.write_short(51)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(index)
        b.write_int(id1)
        b.write_int(id2)
        self.__c.send(b, False)
        return {'ok': True}

    def set_site_dmx_address_by_id(self, site_id, index, id1, id2):
        b = ByteUtil()
        b.write_short(235)
        b.write_int(site_id)
        b.write_int(index)
        b.write_int(id1)
        b.write_int(id2)
        self.__c.send(b, False)
        return {'ok': True}

    def set_cue_play_mode(self, sequence_id, cue_id, play_mode):
        b = ByteUtil()
        b.write_short(53)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_int(play_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def set_next_cue_play_mode(self, sequence_id, play_mode):
        b = ByteUtil()
        b.write_short(54)
        b.write_int(sequence_id)
        b.write_int(play_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def set_ignore_next_cue(self, sequence_id, do_ignore):
        b = ByteUtil()
        b.write_short(55)
        b.write_int(sequence_id)
        b.write_byte(do_ignore)
        self.__c.send(b, False)
        return {'ok': True}

    def save_project(self):
        b = ByteUtil()
        b.write_short(62)
        self.__c.send(b, False)
        return {'ok': True}

    def set_is_site_fullscreen(self, site_id, is_fullscreen):
        b = ByteUtil()
        b.write_short(64)
        b.write_int(site_id)
        b.write_byte(is_fullscreen)
        self.__c.send(b, False)
        return {'ok': True}

    def set_is_site_fullscreen_by_ip(self, ip_address, is_fullscreen):
        b = ByteUtil()
        b.write_short(65)
        b.write_string_narrow(ip_address)
        b.write_byte(is_fullscreen)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_texture_size(self, dmx_folder_id, dmx_file_id, width, height):
        b = ByteUtil()
        b.write_short(66)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(width)
        b.write_int(height)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_properties(self, dmx_folder_id, dmx_file_id, font_family, size, style, alignment, color_red, color_green, color_blue):
        b = ByteUtil()
        b.write_short(67)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(font_family)
        b.write_int(size)
        b.write_byte(style)
        b.write_byte(alignment)
        b.write_byte(color_red)
        b.write_byte(color_green)
        b.write_byte(color_blue)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_center_on_texture(self, dmx_folder_id, dmx_file_id, center_on_texture):
        b = ByteUtil()
        b.write_short(68)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_byte(center_on_texture)
        self.__c.send(b, False)
        return {'ok': True}

    def create_text_input_wide(self, dmx_folder_id, dmx_file_id, text):
        b = ByteUtil()
        b.write_short(69)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_wide(text)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_wide(self, dmx_folder_id, dmx_file_id, text):
        b = ByteUtil()
        b.write_short(70)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_wide(text)
        self.__c.send(b, False)
        return {'ok': True}

    def set_site_ip_by_id(self, site_id, ip):
        b = ByteUtil()
        b.write_short(71)
        b.write_int(site_id)
        b.write_string_narrow(ip)
        self.__c.send(b, False)
        return {'ok': True}

    def get_clip_remaining_time(self, site_id, device_id, sequence_id):
        b = ByteUtil()
        b.write_short(77)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        return d

    def get_remaining_time_until_next_cue(self, sequence_id):
        b = ByteUtil()
        b.write_short(78)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        return d

    def get_resource_count(self):
        b = ByteUtil()
        b.write_short(82)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['mediaCount'] = r.read_int()
        return d

    def get_tree_item_count(self):
        b = ByteUtil()
        b.write_short(150)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemCount'] = r.read_int()
        return d

    def create_project_folder(self, folder_name):
        b = ByteUtil()
        b.write_short(83)
        b.write_string_wide(folder_name)
        self.__c.send(b, False)
        return {'ok': True}

    def create_project_folder_in_path(self, folder_name, project_path):
        b = ByteUtil()
        b.write_short(122)
        b.write_string_wide(folder_name)
        b.write_string_wide(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def create_project_folder_in_tree_item(self, folder_name, tree_item_index):
        b = ByteUtil()
        b.write_short(157)
        b.write_string_wide(folder_name)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_folder_from_project(self, project_path):
        b = ByteUtil()
        b.write_short(123)
        b.write_string_wide(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def set_device_selection(self, site_id, device_id, selection_mode):
        b = ByteUtil()
        b.write_short(86)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(selection_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def set_clx_controller_fader_mapping(self, fader_id, sequence_id):
        b = ByteUtil()
        b.write_short(90)
        b.write_int(fader_id)
        b.write_int(sequence_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_clx_controller_cue_mapping(self, cue_btn_id, sequence_id, cue_id):
        b = ByteUtil()
        b.write_short(92)
        b.write_int(cue_btn_id)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_cue(self, sequence_id, cue_id, hours, minutes, seconds, frames, cue_name, cue_kind_id):
        b = ByteUtil()
        b.write_short(93)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        b.write_string_wide(cue_name)
        b.write_int(cue_kind_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_cue_by_id(self, sequence_id, cue_id):
        b = ByteUtil()
        b.write_short(94)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_all_cues(self, sequence_id):
        b = ByteUtil()
        b.write_short(95)
        b.write_int(sequence_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_video_layer_get_id(self, site_id, is_graphic_layer):
        b = ByteUtil()
        b.write_short(110)
        b.write_int(site_id)
        b.write_bool(is_graphic_layer)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['layerId'] = r.read_int()
        return d

    def remove_layer(self, site_id, layer_id, is_graphic_layer):
        b = ByteUtil()
        b.write_short(97)
        b.write_int(site_id)
        b.write_int(layer_id)
        b.write_bool(is_graphic_layer)
        self.__c.send(b, False)
        return {'ok': True}

    def set_is_backup(self, enable):
        b = ByteUtil()
        b.write_short(102)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def apply_view(self, view_id):
        b = ByteUtil()
        b.write_short(103)
        b.write_int(view_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_spare_from_spread(self, site_id, spare_from_spread):
        b = ByteUtil()
        b.write_short(104)
        b.write_int(site_id)
        b.write_bool(spare_from_spread)
        self.__c.send(b, False)
        return {'ok': True}

    def get_param_resource(self, site_id, device_id, is_media, parameter_name):
        b = ByteUtil()
        b.write_short(105)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_bool(is_media)
        b.write_string_narrow(parameter_name)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['dmxFolderId'] = r.read_int()
        d['dmxFileId'] = r.read_int()
        d['filePath'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        return d

    def get_media_transport_mode(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(108)
        b.write_int(site_id)
        b.write_int(device_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['transportMode'] = r.read_int()
        return d

    def get_is_site_connected(self, site_id):
        b = ByteUtil()
        b.write_short(109)
        b.write_int(site_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isConnected'] = r.read_bool()
        return d

    def move_layer_up(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(111)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def move_layer_down(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(112)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def move_layer_to_first_position(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(113)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def move_layer_to_last_position(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(114)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_enable_clx_controller(self, for_jog_shuttle, enable):
        b = ByteUtil()
        b.write_short(117)
        b.write_byte(for_jog_shuttle)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def get_enable_clx_controller(self, for_jog_shuttle):
        b = ByteUtil()
        b.write_short(116)
        b.write_byte(for_jog_shuttle)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isEnabled'] = r.read_bool()
        return d

    def set_sequence_cue_wait_time(self, sequence_id, cue_id, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(118)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_cue_jump_target_time(self, sequence_id, cue_id, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(119)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_cue_jump_count(self, sequence_id, cue_id, jump_count):
        b = ByteUtil()
        b.write_short(120)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_int(jump_count)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_cue_trigger_count(self, sequence_id, cue_id):
        b = ByteUtil()
        b.write_short(121)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        self.__c.send(b, False)
        return {'ok': True}

    def get_is_content_consistent(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(127)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isContentInconsistent'] = r.read_int()
        return d

    def get_is_content_consistent_by_name(self, resource_path):
        b = ByteUtil()
        b.write_short(128)
        b.write_string_wide(resource_path)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isContentInconsistent'] = r.read_int()
        return d

    def create_sequence_get_id(self):
        b = ByteUtil()
        b.write_short(130)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['sequenceId'] = r.read_int()
        return d

    def remove_sequence(self, sequence_id):
        b = ByteUtil()
        b.write_short(131)
        b.write_int(sequence_id)
        self.__c.send(b, False)
        return {'ok': True}

    def send_mouse_input(self, site_id, device_id, mouse_event_type, screen_pos_x, screen_pos_y, first_pass):
        b = ByteUtil()
        b.write_short(136)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(mouse_event_type)
        b.write_int(screen_pos_x)
        b.write_int(screen_pos_y)
        b.write_bool(first_pass)
        self.__c.send(b, False)
        return {'ok': True}

    def send_mouse_scroll(self, site_id, device_id, scroll_value):
        b = ByteUtil()
        b.write_short(233)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(scroll_value)
        self.__c.send(b, False)
        return {'ok': True}

    def send_touch_input(self, site_id, device_id, touch_id, touch_type, screen_pos_x, screen_pos_y, first_pass):
        b = ByteUtil()
        b.write_short(146)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(touch_id)
        b.write_int(touch_type)
        b.write_int(screen_pos_x)
        b.write_int(screen_pos_y)
        b.write_bool(first_pass)
        self.__c.send(b, False)
        return {'ok': True}

    def send_keyboard_input(self, site_id, keyboard_event_type, key_code):
        b = ByteUtil()
        b.write_short(137)
        b.write_int(site_id)
        b.write_int(keyboard_event_type)
        b.write_int(key_code)
        self.__c.send(b, False)
        return {'ok': True}

    def set_show_cursor_in_fullscreen(self, site_id, show_cursor):
        b = ByteUtil()
        b.write_short(138)
        b.write_int(site_id)
        b.write_bool(show_cursor)
        self.__c.send(b, False)
        return {'ok': True}

    def set_node_of_site_is_audio_clock_master(self, site_id, is_master):
        b = ByteUtil()
        b.write_short(145)
        b.write_int(site_id)
        b.write_bool(is_master)
        self.__c.send(b, False)
        return {'ok': True}

    def add_encryption_key_get_id(self, encryption_key):
        b = ByteUtil()
        b.write_short(164)
        b.write_string_wide(encryption_key)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isKeyAdded'] = r.read_bool()
        return d

    def add_encryption_policy_get_id(self, encryption_policy):
        b = ByteUtil()
        b.write_short(165)
        b.write_string_wide(encryption_policy)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isKeyAdded'] = r.read_bool()
        return d

    def set_route_input_to_layer(self, site_id, enable_input_routing):
        b = ByteUtil()
        b.write_short(166)
        b.write_int(site_id)
        b.write_bool(enable_input_routing)
        self.__c.send(b, False)
        return {'ok': True}

    def set_route_input_to_automation(self, site_id, enable_input_automation):
        b = ByteUtil()
        b.write_short(167)
        b.write_int(site_id)
        b.write_bool(enable_input_automation)
        self.__c.send(b, False)
        return {'ok': True}

    def set_enable_output_for_picking(self, site_id, output_id, enable_input_picking):
        b = ByteUtil()
        b.write_short(168)
        b.write_int(site_id)
        b.write_int(output_id)
        b.write_bool(enable_input_picking)
        self.__c.send(b, False)
        return {'ok': True}

    def set_asio_master_volume(self, site_id, asio_volume):
        b = ByteUtil()
        b.write_short(169)
        b.write_int(site_id)
        b.write_double(asio_volume)
        self.__c.send(b, False)
        return {'ok': True}

    def get_thumbnail_by_path(self, resource_path):
        b = ByteUtil()
        b.write_short(162)
        b.write_string_wide(resource_path)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['thumbnailWidth'] = r.read_int()
        d['thumbnailHeight'] = r.read_int()
        d['thumbnailData'] = r.read_byte_buffer()
        return d

    def get_thumbnail_by_item_index(self, tree_item_index):
        b = ByteUtil()
        b.write_short(163)
        b.write_int(tree_item_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['thumbnailWidth'] = r.read_int()
        d['thumbnailHeight'] = r.read_int()
        d['thumbnailData'] = r.read_byte_buffer()
        return d

    def create_playlist(self, do_set_dmx_ids, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(176)
        b.write_bool(do_set_dmx_ids)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_path(self, project_path, do_set_dmx_ids, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(177)
        b.write_string_narrow(project_path)
        b.write_bool(do_set_dmx_ids)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_item_id(self, tree_item_index, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(178)
        b.write_int(tree_item_index)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_path_from_folder(self, project_path, source_project_path, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(179)
        b.write_string_narrow(project_path)
        b.write_string_narrow(source_project_path)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_tree_item_from_folder(self, tree_item_index, source_folder_item_id, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(180)
        b.write_int(tree_item_index)
        b.write_int(source_folder_item_id)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def push_back_playlist_entry_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, resource_dmx_folder_id, resource_dmx_file_id):
        b = ByteUtil()
        b.write_short(181)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(resource_dmx_folder_id)
        b.write_int(resource_dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def push_back_playlist_entry_by_path(self, playlist_path, resource_path):
        b = ByteUtil()
        b.write_short(182)
        b.write_string_narrow(playlist_path)
        b.write_string_narrow(resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def push_back_playlist_entry_by_item_id(self, playlist_item_index, resource_item_id):
        b = ByteUtil()
        b.write_short(183)
        b.write_int(playlist_item_index)
        b.write_int(resource_item_id)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, resource_dmx_folder_id, resource_dmx_file_id, index):
        b = ByteUtil()
        b.write_short(184)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(resource_dmx_folder_id)
        b.write_int(resource_dmx_file_id)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_by_path(self, playlist_path, resource_path, index):
        b = ByteUtil()
        b.write_short(185)
        b.write_string_narrow(playlist_path)
        b.write_string_narrow(resource_path)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_by_item_id(self, playlist_item_index, resource_item_id, index):
        b = ByteUtil()
        b.write_short(186)
        b.write_int(playlist_item_index)
        b.write_int(resource_item_id)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_playlist_entry_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index):
        b = ByteUtil()
        b.write_short(187)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_playlist_entry_by_path(self, playlist_path, index):
        b = ByteUtil()
        b.write_short(188)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def remove_playlist_entry_by_item_id(self, playlist_item_index, index):
        b = ByteUtil()
        b.write_short(189)
        b.write_int(playlist_item_index)
        b.write_int(index)
        self.__c.send(b, False)
        return {'ok': True}

    def get_playlist_size_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id):
        b = ByteUtil()
        b.write_short(190)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['playlistSize'] = r.read_int()
        return d

    def get_playlist_size_by_path(self, playlist_path):
        b = ByteUtil()
        b.write_short(191)
        b.write_string_narrow(playlist_path)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['playlistSize'] = r.read_int()
        return d

    def get_playlist_size_by_item_id(self, playlist_item_index):
        b = ByteUtil()
        b.write_short(192)
        b.write_int(playlist_item_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['playlistSize'] = r.read_int()
        return d

    def set_playlist_entry_index_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, new_index):
        b = ByteUtil()
        b.write_short(199)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(new_index)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_index_by_path(self, playlist_path, index, new_index):
        b = ByteUtil()
        b.write_short(200)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(new_index)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_index_by_item_id(self, playlist_item_index, index, new_index):
        b = ByteUtil()
        b.write_short(201)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(new_index)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_duration_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(202)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_duration_by_path(self, playlist_path, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(203)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_duration_by_item_id(self, playlist_item_index, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(204)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_fade_out_time_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(205)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_fade_out_time_by_path(self, playlist_path, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(206)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_fade_out_time_by_item_id(self, playlist_item_index, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(207)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_in_point_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(208)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_in_point_by_path(self, playlist_path, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(210)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_in_point_by_item_id(self, playlist_item_index, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(211)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_out_point_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(212)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_out_point_by_path(self, playlist_path, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(213)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_out_point_by_item_id(self, playlist_item_index, index, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(214)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_transition_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, fade_fx_id):
        b = ByteUtil()
        b.write_short(215)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_transition_by_path(self, playlist_path, index, fade_fx_id):
        b = ByteUtil()
        b.write_short(216)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_transition_by_item_id(self, playlist_item_index, index, fade_fx_id):
        b = ByteUtil()
        b.write_short(217)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_note_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, index, p_note):
        b = ByteUtil()
        b.write_short(218)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(index)
        b.write_string_narrow(p_note)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_note_by_path(self, playlist_path, index, p_note):
        b = ByteUtil()
        b.write_short(219)
        b.write_string_narrow(playlist_path)
        b.write_int(index)
        b.write_string_narrow(p_note)
        self.__c.send(b, False)
        return {'ok': True}

    def set_playlist_entry_note_by_item_id(self, playlist_item_index, index, p_note):
        b = ByteUtil()
        b.write_short(220)
        b.write_int(playlist_item_index)
        b.write_int(index)
        b.write_string_narrow(p_note)
        self.__c.send(b, False)
        return {'ok': True}

    def record_live_input_by_dmx_id(self, folder_id, file_id, p_filename, encoding_preset_name, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(222)
        b.write_int(folder_id)
        b.write_int(file_id)
        b.write_string_narrow(p_filename)
        b.write_string_narrow(encoding_preset_name)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def record_live_input_start_by_dmx_id(self, folder_id, file_id, p_filename, encoding_preset_name):
        b = ByteUtil()
        b.write_short(223)
        b.write_int(folder_id)
        b.write_int(file_id)
        b.write_string_narrow(p_filename)
        b.write_string_narrow(encoding_preset_name)
        self.__c.send(b, False)
        return {'ok': True}

    def record_live_input_by_name(self, live_input_resource_path, p_filename, encoding_preset_name, hours, minutes, seconds, frames):
        b = ByteUtil()
        b.write_short(225)
        b.write_string_narrow(live_input_resource_path)
        b.write_string_narrow(p_filename)
        b.write_string_narrow(encoding_preset_name)
        b.write_int(hours)
        b.write_int(minutes)
        b.write_int(seconds)
        b.write_int(frames)
        self.__c.send(b, False)
        return {'ok': True}

    def record_live_input_start_by_name(self, live_input_resource_path, p_filename, encoding_preset_name):
        b = ByteUtil()
        b.write_short(226)
        b.write_string_narrow(live_input_resource_path)
        b.write_string_narrow(p_filename)
        b.write_string_narrow(encoding_preset_name)
        self.__c.send(b, False)
        return {'ok': True}

    def export_video(self, p_filename, encoding_preset_name, sequence_id, start_hour, start_minute, start_second, start_frame, end_hour, end_minute, end_second, end_frame):
        b = ByteUtil()
        b.write_short(227)
        b.write_string_narrow(p_filename)
        b.write_string_narrow(encoding_preset_name)
        b.write_int(sequence_id)
        b.write_int(start_hour)
        b.write_int(start_minute)
        b.write_int(start_second)
        b.write_int(start_frame)
        b.write_int(end_hour)
        b.write_int(end_minute)
        b.write_int(end_second)
        b.write_int(end_frame)
        self.__c.send(b, False)
        return {'ok': True}

    def encode_file_by_name(self, resource_path, encoding_preset):
        b = ByteUtil()
        b.write_short(228)
        b.write_string_narrow(resource_path)
        b.write_string_narrow(encoding_preset)
        self.__c.send(b, False)
        return {'ok': True}

    def encode_file_by_dmx_id(self, folder_id, file_id, encoding_preset):
        b = ByteUtil()
        b.write_short(230)
        b.write_int(folder_id)
        b.write_int(file_id)
        b.write_string_narrow(encoding_preset)
        self.__c.send(b, False)
        return {'ok': True}

    def encode_file_to_path(self, resource_path, project_path, overwrite_existing, encoding_preset):
        b = ByteUtil()
        b.write_short(229)
        b.write_string_narrow(resource_path)
        b.write_string_narrow(project_path)
        b.write_bool(overwrite_existing)
        b.write_string_narrow(encoding_preset)
        self.__c.send(b, False)
        return {'ok': True}

    def encode_file_by_dmx_id(self, folder_id, file_id, project_path, overwrite_existing, encoding_preset):
        b = ByteUtil()
        b.write_short(231)
        b.write_int(folder_id)
        b.write_int(file_id)
        b.write_string_narrow(project_path)
        b.write_bool(overwrite_existing)
        b.write_string_narrow(encoding_preset)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_resolution_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id, width, height):
        b = ByteUtil()
        b.write_short(239)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        b.write_int(width)
        b.write_int(height)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_resolution_by_path(self, canvas_resource_path, width, height):
        b = ByteUtil()
        b.write_short(240)
        b.write_string_narrow(canvas_resource_path)
        b.write_int(width)
        b.write_int(height)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_resolution_by_item_id(self, canvas_item_index, width, height):
        b = ByteUtil()
        b.write_short(241)
        b.write_int(canvas_item_index)
        b.write_int(width)
        b.write_int(height)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_canvas_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id):
        b = ByteUtil()
        b.write_short(242)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_canvas_by_path(self, canvas_resource_path):
        b = ByteUtil()
        b.write_short(243)
        b.write_string_narrow(canvas_resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_canvas_by_item_id(self, canvas_item_index):
        b = ByteUtil()
        b.write_short(244)
        b.write_int(canvas_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def execute_canvas_cmd_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id, cmd, cmd_contains_resource_path):
        b = ByteUtil()
        b.write_short(245)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        b.write_string_narrow(cmd)
        b.write_bool(cmd_contains_resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def execute_canvas_cmd_by_path(self, canvas_resource_path, cmd, cmd_contains_resource_path):
        b = ByteUtil()
        b.write_short(246)
        b.write_string_narrow(canvas_resource_path)
        b.write_string_narrow(cmd)
        b.write_bool(cmd_contains_resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def execute_canvas_cmd_by_item_id(self, canvas_item_index, cmd, cmd_contains_resource_path):
        b = ByteUtil()
        b.write_short(247)
        b.write_int(canvas_item_index)
        b.write_string_narrow(cmd)
        b.write_bool(cmd_contains_resource_path)
        self.__c.send(b, False)
        return {'ok': True}

    def get_canvas_draw_commands_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id):
        b = ByteUtil()
        b.write_short(248)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['commands'] = r.read_string_narrow()
        return d

    def get_canvas_draw_commands_by_path(self, canvas_resource_path):
        b = ByteUtil()
        b.write_short(249)
        b.write_string_narrow(canvas_resource_path)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['commands'] = r.read_string_narrow()
        return d

    def get_canvas_draw_commands_by_item_id(self, canvas_item_index):
        b = ByteUtil()
        b.write_short(250)
        b.write_int(canvas_item_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['commands'] = r.read_string_narrow()
        return d

    def get_media_width_by_dmx_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(251)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['width'] = r.read_int()
        return d

    def get_media_width_by_path(self, folder_path_to_project):
        b = ByteUtil()
        b.write_short(252)
        b.write_string_narrow(folder_path_to_project)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['width'] = r.read_int()
        return d

    def get_media_width_by_item_id(self, item_id):
        b = ByteUtil()
        b.write_short(253)
        b.write_int(item_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['width'] = r.read_int()
        return d

    def get_media_height_by_dmx_id(self, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(254)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['height'] = r.read_int()
        return d

    def get_media_height_by_path(self, folder_path_to_project):
        b = ByteUtil()
        b.write_short(255)
        b.write_string_narrow(folder_path_to_project)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['height'] = r.read_int()
        return d

    def get_media_height_by_item_id(self, item_id):
        b = ByteUtil()
        b.write_short(256)
        b.write_int(item_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['height'] = r.read_int()
        return d

    def get_project_path_on_disc(self):
        b = ByteUtil()
        b.write_short(257)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['commands'] = r.read_string_narrow()
        return d

    def save_project_as(self, folder_path_to_project, project_xml_file_name):
        b = ByteUtil()
        b.write_short(258)
        b.write_string_narrow(folder_path_to_project)
        b.write_string_narrow(project_xml_file_name)
        self.__c.send(b, False)
        return {'ok': True}

    def save_project_copy(self, folder_path_to_project, project_xml_file_name):
        b = ByteUtil()
        b.write_short(259)
        b.write_string_narrow(folder_path_to_project)
        b.write_string_narrow(project_xml_file_name)
        self.__c.send(b, False)
        return {'ok': True}

    def bundle_project(self, bundle_path, bundle_name):
        b = ByteUtil()
        b.write_short(260)
        b.write_string_narrow(bundle_path)
        b.write_string_narrow(bundle_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_resource_name_by_path(self, resource_path, new_resource_name):
        b = ByteUtil()
        b.write_short(261)
        b.write_string_narrow(resource_path)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_resource_name_by_item_index(self, tree_item_index, new_resource_name):
        b = ByteUtil()
        b.write_short(263)
        b.write_int(tree_item_index)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_resource_name_by_dmx_id(self, dmx_folder_id, dmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(262)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def send_canvas_cmds_to_stack_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id, do_add_to_stack):
        b = ByteUtil()
        b.write_short(265)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        b.write_bool(do_add_to_stack)
        self.__c.send(b, False)
        return {'ok': True}

    def set_add_canvas_cmds_to_stack_by_path(self, canvas_resource_path, do_add_to_stack):
        b = ByteUtil()
        b.write_short(266)
        b.write_string_narrow(canvas_resource_path)
        b.write_bool(do_add_to_stack)
        self.__c.send(b, False)
        return {'ok': True}

    def set_add_canvas_cmds_to_stack_by_item_id(self, canvas_item_index, do_add_to_stack):
        b = ByteUtil()
        b.write_short(267)
        b.write_int(canvas_item_index)
        b.write_bool(do_add_to_stack)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_empty_playlist_entries_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id):
        b = ByteUtil()
        b.write_short(268)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_empty_playlist_entries_by_path(self, playlist_path):
        b = ByteUtil()
        b.write_short(269)
        b.write_string_narrow(playlist_path)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_empty_playlist_entries_by_item_id(self, playlist_item_index):
        b = ByteUtil()
        b.write_short(270)
        b.write_int(playlist_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_all_playlist_entries_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id):
        b = ByteUtil()
        b.write_short(271)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_all_playlist_entries_by_path(self, playlist_path):
        b = ByteUtil()
        b.write_short(272)
        b.write_string_narrow(playlist_path)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_all_playlist_entries_by_item_index(self, playlist_item_index):
        b = ByteUtil()
        b.write_short(273)
        b.write_int(playlist_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sublayer_param_of_kind_double(self, site_id, device_id, sublayer_id, parameter_kind_id, parameter_value, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(274)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(sublayer_id)
        b.write_int(parameter_kind_id)
        b.write_double(parameter_value)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def handle_sublayer(self, site_id, device_id, action, data):
        b = ByteUtil()
        b.write_short(275)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(action)
        b.write_int(data)
        self.__c.send(b, False)
        return {'ok': True}

    def set_cue_name(self, sequence_id, cue_id, cue_name):
        b = ByteUtil()
        b.write_short(276)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        b.write_string_narrow(cue_name)
        self.__c.send(b, False)
        return {'ok': True}

    def get_cue_name(self, sequence_id, cue_id):
        b = ByteUtil()
        b.write_short(277)
        b.write_int(sequence_id)
        b.write_int(cue_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['cueName'] = r.read_string_narrow()
        return d

    def store_active_site(self, sequence_id, site_id):
        b = ByteUtil()
        b.write_short(278)
        b.write_int(sequence_id)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def store_active_device(self, sequence_id, site_id, device_id):
        b = ByteUtil()
        b.write_short(279)
        b.write_int(sequence_id)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def store_active_param(self, sequence_id, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(280)
        b.write_int(sequence_id)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_device_by_name(self, site_id, device_id, source_device_id, parameter_name):
        b = ByteUtil()
        b.write_short(282)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(source_device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource_to_param(self, site_id, device_id, dmx_folder_id, dmx_file_id, for_mesh, parameter_name):
        b = ByteUtil()
        b.write_short(283)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(for_mesh)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence(self, folder_path, site_id, dmx_folder_id, dmx_file_id, fps):
        b = ByteUtil()
        b.write_short(284)
        b.write_string_narrow(folder_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(fps)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_to_folder(self, folder_path, site_id, dmx_folder_id, dmx_file_id, fps, project_path):
        b = ByteUtil()
        b.write_short(285)
        b.write_string_narrow(folder_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(fps)
        b.write_string_narrow(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_to_tree_item(self, folder_path, site_id, dmx_folder_id, dmx_file_id, fps, tree_item_index):
        b = ByteUtil()
        b.write_short(286)
        b.write_string_narrow(folder_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(fps)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node(self, folder_path, fps):
        b = ByteUtil()
        b.write_short(287)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node_id(self, folder_path, fps, dmx_folder_id, dmx_file_id):
        b = ByteUtil()
        b.write_short(288)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node_to_folder(self, folder_path, fps, project_path):
        b = ByteUtil()
        b.write_short(289)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        b.write_string_narrow(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node_to_folder_id(self, folder_path, fps, dmx_folder_id, dmx_file_id, project_path):
        b = ByteUtil()
        b.write_short(290)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(project_path)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node_to_tree_item(self, folder_path, fps, tree_item_index):
        b = ByteUtil()
        b.write_short(291)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def add_image_sequence_from_local_node_to_tree_item_id(self, folder_path, fps, dmx_folder_id, dmx_file_id, tree_item_index):
        b = ByteUtil()
        b.write_short(292)
        b.write_string_narrow(folder_path)
        b.write_int(fps)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_formatted(self, dmx_folder_id, dmx_file_id, text, is_formatted):
        b = ByteUtil()
        b.write_short(293)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(text)
        b.write_bool(is_formatted)
        self.__c.send(b, False)
        return {'ok': True}

    def set_text_formatted_wide(self, dmx_folder_id, dmx_file_id, text, is_formatted):
        b = ByteUtil()
        b.write_short(294)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_wide(text)
        b.write_bool(is_formatted)
        self.__c.send(b, False)
        return {'ok': True}

    def get_current_time_cue_info(self, sequence_id):
        b = ByteUtil()
        b.write_short(295)
        b.write_int(sequence_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        d['previousCueId'] = r.read_int()
        d['previousCueName'] = r.read_string_narrow()
        d['hoursPreviousCue'] = r.read_int()
        d['minutesPreviousCue'] = r.read_int()
        d['secondsPreviousCue'] = r.read_int()
        d['framesPreviousCue'] = r.read_int()
        d['previousCueMode'] = r.read_int()
        d['nextCueId'] = r.read_int()
        d['nextCueName'] = r.read_string_narrow()
        d['hoursNextCue'] = r.read_int()
        d['minutesNextCue'] = r.read_int()
        d['secondsNextCue'] = r.read_int()
        d['framesNextCue'] = r.read_int()
        d['nextCueMode'] = r.read_int()
        return d

    def get_content_is_consistent_by_tree_item(self, tree_item_index):
        b = ByteUtil()
        b.write_short(296)
        b.write_int(tree_item_index)
        self.__c.send(b, False)
        return {'ok': True}

    def spread_to_site(self, resource_path, site_id):
        b = ByteUtil()
        b.write_short(297)
        b.write_string_narrow(resource_path)
        b.write_int(site_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_group_selection(self, group_index, selection_mode):
        b = ByteUtil()
        b.write_short(298)
        b.write_int(group_index)
        b.write_int(selection_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def set_sequence_selection(self, sequence_id):
        b = ByteUtil()
        b.write_short(299)
        b.write_int(sequence_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_with_name(self, do_set_dmx_ids, dmx_folder_id, dmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(300)
        b.write_bool(do_set_dmx_ids)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_path_with_name(self, project_path, do_set_dmx_ids, dmx_folder_id, dmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(301)
        b.write_string_narrow(project_path)
        b.write_bool(do_set_dmx_ids)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_item_id_with_name(self, tree_item_index, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(302)
        b.write_int(tree_item_index)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_path_from_folder_with_name(self, project_path, source_project_path, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(303)
        b.write_string_narrow(project_path)
        b.write_string_narrow(source_project_path)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def create_playlist_in_tree_item_from_folder_with_name(self, tree_item_index, source_folder_item_id, setdmx_file_ids, new_dmx_folder_id, newdmx_file_id, new_resource_name):
        b = ByteUtil()
        b.write_short(304)
        b.write_int(tree_item_index)
        b.write_int(source_folder_item_id)
        b.write_bool(setdmx_file_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        b.write_string_narrow(new_resource_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_watched_folder_property(self, project_path, watch_folder_property, enable):
        b = ByteUtil()
        b.write_short(305)
        b.write_string_narrow(project_path)
        b.write_int(watch_folder_property)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def set_watched_folder_property_by_item_id(self, tree_item_index, watch_folder_property, enable):
        b = ByteUtil()
        b.write_short(306)
        b.write_int(tree_item_index)
        b.write_int(watch_folder_property)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def set_folder_spread_to_site(self, project_path, site_id, enable):
        b = ByteUtil()
        b.write_short(307)
        b.write_string_narrow(project_path)
        b.write_int(site_id)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def set_folder_spread_to_site_by_item_id(self, tree_item_index, site_id, enable):
        b = ByteUtil()
        b.write_short(308)
        b.write_int(tree_item_index)
        b.write_int(site_id)
        b.write_bool(enable)
        self.__c.send(b, False)
        return {'ok': True}

    def clear_streaming_text(self, dmx_folder_id, dmx_file_id, pending_only):
        b = ByteUtil()
        b.write_short(309)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(pending_only)
        self.__c.send(b, False)
        return {'ok': True}

    def get_watched_folder_property(self, project_path, watch_folder_property):
        b = ByteUtil()
        b.write_short(310)
        b.write_string_narrow(project_path)
        b.write_int(watch_folder_property)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isEnabled'] = r.read_bool()
        return d

    def get_watched_folder_property_by_item_id(self, tree_item_index, watch_folder_property):
        b = ByteUtil()
        b.write_short(311)
        b.write_int(tree_item_index)
        b.write_int(watch_folder_property)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isEnabled'] = r.read_bool()
        return d

    def get_folder_spread_to_site(self, project_path, site_id):
        b = ByteUtil()
        b.write_short(312)
        b.write_string_narrow(project_path)
        b.write_int(site_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isEnabled'] = r.read_bool()
        return d

    def get_folder_spread_to_site_by_item_id(self, tree_item_index, site_id):
        b = ByteUtil()
        b.write_short(313)
        b.write_int(tree_item_index)
        b.write_int(site_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['isEnabled'] = r.read_bool()
        return d

    def insert_playlist_entry_with_parameters_by_dmx_id(self):
        b = ByteUtil()
        b.write_short(314)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_with_parameters_by_path(self):
        b = ByteUtil()
        b.write_short(315)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_with_parameters_by_tree_item(self):
        b = ByteUtil()
        b.write_short(316)
        self.__c.send(b, False)
        return {'ok': True}

    def set_param_relative(self, site_id, device_id, parameter_name, parameter_value):
        b = ByteUtil()
        b.write_short(18)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        b.write_int(parameter_value)
        self.__c.send(b, False)
        return {'ok': True}

    def add_content(self, file_path, site_id, dmx_folder_id, dmx_file_id, auto_increment_dmx_id):
        b = ByteUtil()
        b.write_short(19)
        b.write_string_narrow(file_path)
        b.write_int(site_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(auto_increment_dmx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def get_media_info(self, tree_items_media_index):
        b = ByteUtil()
        b.write_short(76)
        b.write_int(tree_items_media_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['dmxFolderId'] = r.read_int()
        d['dmxFileId'] = r.read_int()
        d['resourceName'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        d['projectPath'] = r.read_string_narrow()
        d['width'] = r.read_int()
        d['height'] = r.read_int()
        d['fps'] = r.read_int()
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        d['options'] = r.read_int()
        return d

    def insert_playlist_entry_with_parameters_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, resource_dmx_folder_id, resource_dmx_file_id, index, duration_hours, duration_minutes, duration_seconds, duration_frames, fade_out_hour, fade_out_minute, fade_out_second, fade_out_frame, start_hour, start_minute, start_second, start_frame, end_hour, end_minute, end_second, end_frame, fade_fx_id):
        b = ByteUtil()
        b.write_short(314)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(resource_dmx_folder_id)
        b.write_int(resource_dmx_file_id)
        b.write_int(index)
        b.write_int(duration_hours)
        b.write_int(duration_minutes)
        b.write_int(duration_seconds)
        b.write_int(duration_frames)
        b.write_int(fade_out_hour)
        b.write_int(fade_out_minute)
        b.write_int(fade_out_second)
        b.write_int(fade_out_frame)
        b.write_int(start_hour)
        b.write_int(start_minute)
        b.write_int(start_second)
        b.write_int(start_frame)
        b.write_int(end_hour)
        b.write_int(end_minute)
        b.write_int(end_second)
        b.write_int(end_frame)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_with_parameters_by_path(self, playlist_path, resource_path, index, duration_hours, duration_minutes, duration_seconds, duration_frames, fade_out_hour, fade_out_minute, fade_out_second, fade_out_frame, start_hour, start_minute, start_second, start_frame, end_hour, end_minute, end_second, end_frame, fade_fx_id):
        b = ByteUtil()
        b.write_short(315)
        b.write_string_narrow(playlist_path)
        b.write_string_narrow(resource_path)
        b.write_int(index)
        b.write_int(duration_hours)
        b.write_int(duration_minutes)
        b.write_int(duration_seconds)
        b.write_int(duration_frames)
        b.write_int(fade_out_hour)
        b.write_int(fade_out_minute)
        b.write_int(fade_out_second)
        b.write_int(fade_out_frame)
        b.write_int(start_hour)
        b.write_int(start_minute)
        b.write_int(start_second)
        b.write_int(start_frame)
        b.write_int(end_hour)
        b.write_int(end_minute)
        b.write_int(end_second)
        b.write_int(end_frame)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def insert_playlist_entry_with_parameters_by_tree_item(self, playlist_item_index, resource_item_id, index, duration_hours, duration_minutes, duration_seconds, duration_frames, fade_out_hour, fade_out_minute, fade_out_second, fade_out_frame, start_hour, start_minute, start_second, start_frame, end_hour, end_minute, end_second, end_frame, fade_fx_id):
        b = ByteUtil()
        b.write_short(316)
        b.write_int(playlist_item_index)
        b.write_int(resource_item_id)
        b.write_int(index)
        b.write_int(duration_hours)
        b.write_int(duration_minutes)
        b.write_int(duration_seconds)
        b.write_int(duration_frames)
        b.write_int(fade_out_hour)
        b.write_int(fade_out_minute)
        b.write_int(fade_out_second)
        b.write_int(fade_out_frame)
        b.write_int(start_hour)
        b.write_int(start_minute)
        b.write_int(start_second)
        b.write_int(start_frame)
        b.write_int(end_hour)
        b.write_int(end_minute)
        b.write_int(end_second)
        b.write_int(end_frame)
        b.write_int(fade_fx_id)
        self.__c.send(b, False)
        return {'ok': True}

    def set_yaw_pitch_roll(self, site_id, device_id, in_radians, yaw, pitch, roll, do_silent, do_direct):
        b = ByteUtil()
        b.write_short(323)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_bool(in_radians)
        b.write_double(yaw)
        b.write_double(pitch)
        b.write_double(roll)
        b.write_bool(do_silent)
        b.write_bool(do_direct)
        self.__c.send(b, False)
        return {'ok': True}

    def get_yaw_pitch_roll(self, site_id, device_id, in_radians):
        b = ByteUtil()
        b.write_short(324)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_bool(in_radians)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['yaw'] = r.read_double()
        d['pitch'] = r.read_double()
        d['roll'] = r.read_double()
        return d

    def get_site_ids(self):
        b = ByteUtil()
        b.write_short(317)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['siteIds'] = r.read_int_buffer()
        return d

    def set_compositing_pass_render_target_size(self, site_id, device_id, width, height):
        b = ByteUtil()
        b.write_short(341)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(width)
        b.write_int(height)
        self.__c.send(b, False)
        return {'ok': True}

    def set_softedge_is_warped(self, site_id, device_id, is_warped):
        b = ByteUtil()
        b.write_short(342)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_bool(is_warped)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_texture_format_by_dmx_id(self, canvas_dmx_folder_id, canvas_dmx_file_id, texture_format):
        b = ByteUtil()
        b.write_short(338)
        b.write_int(canvas_dmx_folder_id)
        b.write_int(canvas_dmx_file_id)
        b.write_int(texture_format)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_texture_format_by_path(self, canvas_resource_path, texture_format):
        b = ByteUtil()
        b.write_short(339)
        b.write_string_narrow(canvas_resource_path)
        b.write_int(texture_format)
        self.__c.send(b, False)
        return {'ok': True}

    def set_canvas_texture_format_by_item_id(self, canvas_item_index, texture_format):
        b = ByteUtil()
        b.write_short(340)
        b.write_int(canvas_item_index)
        b.write_int(texture_format)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_sockets(self):
        b = ByteUtil()
        b.write_short(354)
        self.__c.send(b, False)
        return {'ok': True}

    def reset_serial_link(self, site_id, device_id):
        b = ByteUtil()
        b.write_short(355)
        b.write_int(site_id)
        b.write_int(device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource_to_param_blocked(self, site_id, device_id, dmx_folder_id, dmx_file_id, for_mesh, parameter_name):
        b = ByteUtil()
        b.write_short(352)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(for_mesh)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_resource_blocked(self, site_id, device_id, dmx_folder_id, dmx_file_id, for_mesh):
        b = ByteUtil()
        b.write_short(353)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(dmx_folder_id)
        b.write_int(dmx_file_id)
        b.write_bool(for_mesh)
        self.__c.send(b, False)
        return {'ok': True}

    def jump_to_play_list_entry_by_dmx_id(self, forward, playlist_dmx_folder_id, playlistdmx_file_id, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(356)
        b.write_bool(forward)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def jump_to_play_list_entry_by_path(self, forward, playlist_path, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(357)
        b.write_bool(forward)
        b.write_string_narrow(playlist_path)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def jump_to_play_list_entry_by_item_id(self, forward, playlist_item_index, site_id, device_id, parameter_name):
        b = ByteUtil()
        b.write_short(358)
        b.write_bool(forward)
        b.write_int(playlist_item_index)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_string_narrow(parameter_name)
        self.__c.send(b, False)
        return {'ok': True}

    def set_media_transport_mode(self, site_id, device_id, transport_mode):
        b = ByteUtil()
        b.write_short(359)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(transport_mode)
        self.__c.send(b, False)
        return {'ok': True}

    def assign_device(self, site_id, device_id, source_device_id):
        b = ByteUtil()
        b.write_short(281)
        b.write_int(site_id)
        b.write_int(device_id)
        b.write_int(source_device_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_canvas(self, do_set_dmx_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(236)
        b.write_bool(do_set_dmx_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_canvas_by_path(self, canvas_resource_path, do_set_dmx_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(237)
        b.write_string_narrow(canvas_resource_path)
        b.write_bool(do_set_dmx_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def create_canvas_by_item_id(self, folder_item_index, do_set_dmx_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(238)
        b.write_int(folder_item_index)
        b.write_bool(do_set_dmx_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def record_live_input_stop(self):
        b = ByteUtil()
        b.write_short(224)
        self.__c.send(b, False)
        return {'ok': True}

    def create_canvas_by_path_from_template(self, canvas_resource_path, new_resource_name, cmd, set_dims, width, height, do_set_dmx_ids, new_dmx_folder_id, newdmx_file_id):
        b = ByteUtil()
        b.write_short(264)
        b.write_string_narrow(canvas_resource_path)
        b.write_string_narrow(new_resource_name)
        b.write_string_narrow(cmd)
        b.write_bool(set_dims)
        b.write_int(width)
        b.write_int(height)
        b.write_bool(do_set_dmx_ids)
        b.write_int(new_dmx_folder_id)
        b.write_int(newdmx_file_id)
        self.__c.send(b, False)
        return {'ok': True}

    def get_host_revision_number(self):
        b = ByteUtil()
        b.write_short(334)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['revision'] = r.read_int()
        return d

    def get_tree_item_info(self, tree_item_index):
        b = ByteUtil()
        b.write_short(151)
        b.write_int(tree_item_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['resourceType'] = r.read_int()
        d['resourcePath'] = r.read_string_wide()
        d['folderPath'] = r.read_string_wide()
        return d

    def get_media_info_by_tree_item_index(self, index):
        b = ByteUtil()
        b.write_short(152)
        b.write_int(index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['dmxFolderId'] = r.read_int()
        d['dmxFileId'] = r.read_int()
        d['resourceName'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        d['projectPath'] = r.read_string_narrow()
        d['width'] = r.read_int()
        d['height'] = r.read_int()
        d['fps'] = r.read_int()
        d['hours'] = r.read_int()
        d['minutes'] = r.read_int()
        d['seconds'] = r.read_int()
        d['frames'] = r.read_int()
        d['options'] = r.read_int()
        return d

    def get_playlist_entry_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id, playlist_entry_index):
        b = ByteUtil()
        b.write_short(193)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        b.write_int(playlist_entry_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIndex'] = r.read_int()
        d['resourceName'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        d['durationHours'] = r.read_int()
        d['durationMinutes'] = r.read_int()
        d['durationSeconds'] = r.read_int()
        d['durationFrames'] = r.read_int()
        d['fadeOutHour'] = r.read_int()
        d['fadeOutMinute'] = r.read_int()
        d['fadeOutSecond'] = r.read_int()
        d['fadeOutFrame'] = r.read_int()
        d['startHour'] = r.read_int()
        d['startMinute'] = r.read_int()
        d['startSecond'] = r.read_int()
        d['startFrame'] = r.read_int()
        d['endHour'] = r.read_int()
        d['endMinute'] = r.read_int()
        d['endSecond'] = r.read_int()
        d['endFrame'] = r.read_int()
        d['fadeFxId'] = r.read_int()
        return d

    def get_playlist_entry_by_path(self, playlist_path, playlist_entry_index):
        b = ByteUtil()
        b.write_short(194)
        b.write_string_narrow(playlist_path)
        b.write_int(playlist_entry_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIndex'] = r.read_int()
        d['resourceName'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        d['durationHours'] = r.read_int()
        d['durationMinutes'] = r.read_int()
        d['durationSeconds'] = r.read_int()
        d['durationFrames'] = r.read_int()
        d['fadeOutHour'] = r.read_int()
        d['fadeOutMinute'] = r.read_int()
        d['fadeOutSecond'] = r.read_int()
        d['fadeOutFrame'] = r.read_int()
        d['startHour'] = r.read_int()
        d['startMinute'] = r.read_int()
        d['startSecond'] = r.read_int()
        d['startFrame'] = r.read_int()
        d['endHour'] = r.read_int()
        d['endMinute'] = r.read_int()
        d['endSecond'] = r.read_int()
        d['endFrame'] = r.read_int()
        d['fadeFxId'] = r.read_int()
        return d

    def get_playlist_entry_by_item_id(self, playlist_item_index, playlist_entry_index):
        b = ByteUtil()
        b.write_short(195)
        b.write_int(playlist_item_index)
        b.write_int(playlist_entry_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIndex'] = r.read_int()
        d['resourceName'] = r.read_string_narrow()
        d['resourcePath'] = r.read_string_narrow()
        d['durationHours'] = r.read_int()
        d['durationMinutes'] = r.read_int()
        d['durationSeconds'] = r.read_int()
        d['durationFrames'] = r.read_int()
        d['fadeOutHour'] = r.read_int()
        d['fadeOutMinute'] = r.read_int()
        d['fadeOutSecond'] = r.read_int()
        d['fadeOutFrame'] = r.read_int()
        d['startHour'] = r.read_int()
        d['startMinute'] = r.read_int()
        d['startSecond'] = r.read_int()
        d['startFrame'] = r.read_int()
        d['endHour'] = r.read_int()
        d['endMinute'] = r.read_int()
        d['endSecond'] = r.read_int()
        d['endFrame'] = r.read_int()
        d['fadeFxId'] = r.read_int()
        return d

    def get_playlist_entry_indices_by_dmx_id(self, playlist_dmx_folder_id, playlistdmx_file_id):
        b = ByteUtil()
        b.write_short(196)
        b.write_int(playlist_dmx_folder_id)
        b.write_int(playlistdmx_file_id)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIds'] = r.read_int_buffer()
        return d

    def get_playlist_entry_indices_by_path(self, playlist_path):
        b = ByteUtil()
        b.write_short(197)
        b.write_string_narrow(playlist_path)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIds'] = r.read_int_buffer()
        return d

    def get_playlist_entry_indices_by_item_id(self, playlist_item_index):
        b = ByteUtil()
        b.write_short(198)
        b.write_int(playlist_item_index)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['treeItemIds'] = r.read_int_buffer()
        return d

    def create_graphic_layer_get_id(self, site_id, is_graphic_layer):
        b = ByteUtil()
        b.write_short(96)
        b.write_int(site_id)
        b.write_bool(is_graphic_layer)
        r = self.__c.send(b, True)
        if not r: return {'ok': False, 'code': -1}
        c = r.read_short()
        if c < 0: return {'ok': False, 'code': c, 'error': r.read_int()}
        d = {'ok': True, 'code': c}
        d['layerId'] = r.read_int()
        return d



class Connector(object):
    pass


class OfflineTcp(Connector):
    def __init__(self, domain=0, callback=print, data_format='hex'):
        self.domain, self.callback, self.data_format = domain, callback, data_format

    def format(self, data):
        if self.data_format == 'hex':
            return ''.join('{:02x}'.format(x) for x in data)
        elif self.data_format == 'cpp':
            return "{" + ', '.join('0x{:02x}'.format(x) for x in data) + "}"
        elif self.data_format == 'wd':
            return ''.join('[h{:02x}]'.format(x) for x in data)
        elif self.data_format == 'pb':
            return ' '.join('{:02x}'.format(x) for x in data)
        else:
            raise Exception("Not a format: '%s'" % self.data_format)

    def send(self, data, wait_for_response):
        header = struct.pack("!BlhlB", 1, self.domain, len(data), 0, 0)
        checksum = struct.pack("!B", sum(bytearray(header)) % 255)
        data = b'PBAU' + header + checksum + bytes(data)
        self.callback(self.format(data))


class Tcp(Connector):
    PORT = 6211

    def __init__(self, ip, domain=0):
        self.__ip, self.domain = ip, domain
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # TODO # improve connection handling
        self.__sock.connect((self.__ip, self.PORT))

    def send(self, data, wait_for_response):
        # header consists of magic "PBAU" sequence
        # + protocol version (byte, currently 1)
        # + domain id (integer)
        # + message size (short)
        # + connection id (int, user definable, defaults to 0)
        # + protocol flag (byte, 0 for TCP)
        # + checksum (byte)

        header = struct.pack("!BlhlB", 1, self.domain, len(data), 0, 0)

        checksum = struct.pack("!B", sum(bytearray(header)) % 255)
        self.__sock.sendall(b'PBAU' + header + checksum + bytes(data))

        if wait_for_response:
            # receive only header (17 bytes)
            # TODO # WARNING: This does not take into account
            # TODO # cases where socket.recv returns less than 16
            # TODO # in practice this will never happen though.
            header = self.__sock.recv(17)

            # check for magic bytes...
            if header[0:4] == b'PBAU':
                # ...then parse the rest
                header_parsed = struct.unpack("!4sBlhlBB", header)
                response_length = header_parsed[3]

                return ByteUtil(self.__sock.recv(response_length))

        # if not wait_for_response OR invalid response:
        return ByteUtil()


class ByteUtil:
    def __init__(self, data=None):
        self.__data = data or bytearray()
        self.__pos = 0

    def write_bool(self, val):
        self.__data.extend(struct.pack('!B', val))

    def write_short(self, val):
        self.__data.extend(struct.pack('!h', val))

    def write_int(self, val):
        self.__data.extend(struct.pack('!l', val))

    def write_int64(self, val):
        self.__data.extend(struct.pack('!q', val))

    def write_double(self, val):
        self.__data.extend(struct.pack('d', val))

    def write_string_narrow(self, val):
        self.__data.extend(struct.pack('!h', len(val)))
        self.__data.extend(struct.pack("!%is" % len(val), val.encode("ASCII")))

    def write_string_wide(self, val):
        self.__data.extend(struct.pack('!h', len(val)))
        self.__data.extend(struct.pack("!%is" % len(val), val.encode("UTF-16-BE")))

    def write_byte_buffer(self, val):
        self.__data.extend(struct.pack('!l', len(val)))
        self.__data.extend(struct.pack("!%is" % len(val), val))

    def write_int_buffer(self, val):
        self.__data.extend(struct.pack('!l', len(val)))
        self.__data.extend(struct.pack("!%il" % len(val), val))

    def read_bool(self):
        return self._read_block(1)[0] == 1

    def read_byte(self):
        return self._read_block(1)[0]

    def read_short(self):
        return struct.unpack("!h", self._read_block(2))[0]

    def read_int(self):
        return struct.unpack("!l", self._read_block(4))[0]

    def read_int64(self):
        return struct.unpack("!q", self._read_block(8))[0]

    def read_double(self):
        return struct.unpack("d", self._read_block(8))[0]

    def read_string_narrow(self):
        length = self.read_short()
        return self._read_block(length).decode("ASCII")

    def read_string_wide(self):
        length = self.read_short()
        return self._read_block(length * 2).decode("UTF-16-BE")

    def read_byte_buffer(self):
        length = self.read_int()
        return self._read_block(length)

    def _read_block(self, count):
        self.__pos += count
        if self.__pos > len(self.__data):
            raise IndexError
        return self.__data[self.__pos - count: self.__pos]

    def __bool__(self):
        return not len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

    # Python 2 hooray
    def __str__(self):
        return str(self.__data)

    def __bytes__(self):
        return bytes(self.__data)