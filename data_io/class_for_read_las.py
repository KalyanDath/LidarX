import numpy as np

class ReadLas:
    legacy_number_of_point_records = None
    header = None
    point_data = None
    X = None
    Y = None
    Z = None
    header_data_type = np.dtype([
                            ('file_signature',np.dtype('<u1'),4),
                            ('file_source_id',np.dtype('<u2'),1),
                            ('global_encoding',np.dtype('<u2'),1),
                            ('project_guid_data_1',np.dtype('<u4'),1),
                            ('project_guid_data_2',np.dtype('<u2'),1),
                            ('project_guid_data_3',np.dtype('<u2'),1),
                            ('project_guid_data_4',np.dtype('<u1'),8),
                            ('version_major',np.dtype('<u1'),1),
                            ('version_minor',np.dtype('<u1'),1),
                            ('system_identifier',np.dtype('<u1'),32),
                            ('generating_software',np.dtype('<u1'),32),
                            ('file_creation_day_of_year',np.dtype('<u2'),1),
                            ('file_creation_year',np.dtype('<u2'),1),
                            ('header_size',np.dtype('<u2'),1),
                            ('offset_to_point_data',np.dtype('<u4'),1),
                            ('number_of_variable_length_records',np.dtype('<u4'),1),
                            ('point_data_record_format',np.dtype('<u1'),1),
                            ('point_data_record_length',np.dtype('<u2'),1),
                            ('legacy_number_of_point_records',np.dtype('<u4'),1),
                            ('legacy_number_of_points_by_return',np.dtype('<u4'),5),
                            ('x_scale_factor',np.dtype('<f8'),1),
                            ('y_scale_factor',np.dtype('<f8'),1),
                            ('z_scale_factor',np.dtype('<f8'),1),
                            ('x_offset',np.dtype('<f8'),1),
                            ('y_offset',np.dtype('<f8'),1),
                            ('z_offset',np.dtype('<f8'),1),
                            ('x_max',np.dtype('<f8'),1),
                            ('x_min',np.dtype('<f8'),1),
                            ('y_max',np.dtype('<f8'),1),
                            ('y_min',np.dtype('<f8'),1),
                            ('z_max',np.dtype('<f8'),1),
                            ('z_min',np.dtype('<f8'),1),
                            ])       


    point_data_types0 = np.dtype([
                              ('X', np.int32),
                              ('Y', np.int32),
                              ('Z', np.int32),
                              ('intensity', np.uint16),
                              ('flag_bytes', np.uint8),
                              ('classification', np.uint8),
                              ('scan_angle_rank', np.int8),
                              ('user_data', np.uint8),
                              ('pt_src_id', np.uint16),
                            ])
    point_data_types1 = np.dtype([
                                ('X', np.int32),
                                ('Y', np.int32),
                                ('Z', np.int32),
                                ('intensity', np.uint16),
                                ('flag_bytes', np.uint8),
                                ('classification', np.uint8),
                                ('scale_angle_rank',np.uint8),
                                ('user_data', np.uint8),
                                ('pt_src_id', np.uint16),
                                ('gps_time', np.float64),
                            ])
    point_data_types2 = np.dtype([
                                ('X', np.int32),
                                ('Y', np.int32),
                               ('Z', np.int32),
                               ('intensity', np.uint16),
                               ('return_number', np.uint8),
                               ('flag_bytes', np.uint8),
                               ('classification', np.uint8),
                               ('scan_angle_rank', np.int8),
                               ('user_data', np.uint8),
                               ('pt_src_id', np.uint16),
                               ('red',np.uint16),
                               ('green',np.uint16),
                               ('blue',np.uint16),
                            ])        
    point_data_types3 = np.dtype([
                                ('X', np.int32),
                                ('Y', np.int32),
                                ('Z', np.int32),
                                ('intensity', np.uint16),
                                ('return_number', np.uint8),
                                ('flag_bytes', np.uint8),
                                ('classification', np.uint8),
                                ('scan_angle_rank', np.int8),
                                ('user_data', np.uint8),
                                ('pt_src_id', np.uint16),
                                ('gps_time', np.float64),
                                ('red',np.uint16),
                                ('green',np.uint16),
                                ('blue',np.uint16),
                            ])
    point_data_types4 = np.dtype([
                                ('X', np.int32),
                                ('Y', np.int32),
                                ('Z', np.int32),
                                ('intensity', np.uint16),
                                ('return_number_and_other_data', np.uint8),
                                ('classification', np.uint8),
                                ('scan_angle_rank', np.int8),
                                ('user_data', np.uint8),
                                ('pt_src_id', np.uint16),
                                ('gps_time', np.float64),
                                ('wave-packet_descriptor_index', np.uint8),
                                ('byte_offset_to_waveform_data', np.uint64),
                                ('waveform_packet_size_in_bytes', np.uint32),
                                ('return_point_waveform_location', np.float32),
                                ('x_t', np.float32),
                                ('y_t', np.float32),
                                ('z_t', np.float32),
                                ])
    point_data_types5 = np.dtype([      #
                                ('X', np.int32),
                                ('Y', np.int32),
                                ('Z', np.int32),
                                ('intensity', np.uint16),
                                ('return_number_and_other_data', np.uint8),
                                ('classification', np.uint8),
                                ('scan_angle_rank', np.int8),
                                ('user_data', np.uint8),
                                ('pt_src_id', np.uint16),
                                ('gps_time', np.float64),
                                ('red',np.uint16),
                                ('green',np.uint16),
                                ('blue',np.uint16),
                                ('wave_packet_descriptor_index', np.uint8),
                                ('byte_offset_to_waveform_data', np.uint64),
                                ('waveform_packet_size_in_bytes', np.uint32),
                                ('return_point_waveform_location', np.float32),
                                ('x_t', np.float32),
                                ('y_t', np.float32),
                                ('z_t', np.float32),
                                ])
    point_data_types6 = np.dtype([     #30
                                ('X', np.int32),
                                ('Y', np.int32),
                                ('Z', np.int32),
                                ('intensity', np.uint16),
                                ('return_number_and_number_of_returns', np.uint8),
                                ('flag_bytes', np.uint8),
                                ('classification', np.uint8),
                                ('user_data', np.uint8),
                                ('scan_angle', np.int16),
                                ('pt_src_id', np.uint16),
                                ('gps_time', np.float64),
                                ])
    def __init__(self,filename):
        self.file = open(filename,'rb')
        self.filename = filename
        self.read_header()
        self.read_point_data()
        
    def read_header(self):
        self.file.seek(0)
        self.header = np.fromfile(self.file,self.header_data_type,1)
        self.file_signature = self.header['file_signature']
        self.file_source_id = self.header['file_source_id']
        self.global_encoding = self.header['global_encoding']
        self.project_guid_data_1 = self.header['project_guid_data_1']
        self.project_guid_data_2 = self.header['project_guid_data_2']
        self.project_guid_data_3 = self.header['project_guid_data_3']
        self.project_guid_data_4 = self.header['project_guid_data_4']
        self.version_major = self.header['version_major']
        self.version_minor = self.header['version_minor']
        self.system_identifier = self.header['system_identifier']
        self.generating_software = self.header['generating_software']
        self.file_creation_day_of_year = self.header['file_creation_day_of_year']
        self.file_creation_year = self.header['file_creation_year']
        self.header_size = self.header['header_size']
        self.offset_to_point_data = self.header['offset_to_point_data']
        self.number_of_variable_length_records = self.header['number_of_variable_length_records']
        self.point_data_record_format = self.header['point_data_record_format']
        self.point_data_record_length = self.header['point_data_record_length']
        self.legacy_number_of_point_records = self.header['legacy_number_of_point_records']
        self.legacy_number_of_points_by_return = self.header['legacy_number_of_points_by_return']
        self.x_scale_factor = self.header['x_scale_factor']
        self.y_scale_factor = self.header['y_scale_factor']
        self.z_scale_factor = self.header['z_scale_factor']
        self.x_offset = self.header['x_offset']
        self.y_offset = self.header['y_offset']
        self.z_offset = self.header['z_offset']
        self.max_x = self.header['x_max']
        self.min_x = self.header['y_max']
        self.max_y = self.header['z_max']
        self.min_y = self.header['x_min']
        self.max_z = self.header['y_min']
        self.min_z = self.header['z_min']
        

        
    def read_point_data(self):
        self.file.seek(self.header['offset_to_point_data'][0])
        print("KKKKKKKKKKKKKKKK",self.header['point_data_record_length'])
        if self.header['point_data_record_length'] == 28:
            point_data_types = self.point_data_types0
        elif self.header['point_data_record_length'] == 35:
            point_data_types = self.point_data_types1
        elif self.header['point_data_record_length'] == 33:
            point_data_types = self.point_data_types2
        elif self.header['point_data_record_length'] == 41:
            point_data_types = self.point_data_types3
        elif self.header['point_data_record_length'] == 57:
            point_data_types = self.point_data_types4
        elif self.header['point_data_record_length'] == 63:
            point_data_types = self.point_data_types5
        elif self.header['point_data_record_length'] == 30:
            point_data_types = self.point_data_types6
        self.file.seek(self.header['offset_to_point_data'][0])
        self.point_data = np.fromfile(self.file, dtype=point_data_types, count=self.header['legacy_number_of_point_records'][0])
        #print(self.point_data['X'])
        self.X = np.array(self.point_data['X']*self.header['x_scale_factor'] + self.header['x_offset'])
        self.Y = np.array(self.point_data['Y']*self.header['y_scale_factor'] + self.header['y_offset'])
        self.Z = np.array(self.point_data['Z']*self.header['z_scale_factor'] + self.header['z_offset'])
        self.intensity = self.point_data['intensity']
        
        self.flag_bytes = self.point_data['flag_bytes']
        self.classification = self.point_data['classification']
        self.scan_angle_rank = self.point_data['scan_angle_rank']
        self.user_data = self.point_data['user_data']
        self.pt_src_id = self.point_data['pt_src_id']
        try:
            self.red = self.point_data['red']
            self.green = self.point_data['green']
            self.blue = self.point_data['blue']
        except:
            print("No RGB values")
        try:
            self.gps_time = self.point_data['gps_time']
        except:
            print("No GPS time")
        try:
            self.return_number = self.point_data['return_number']
        except:
            print("No return number")