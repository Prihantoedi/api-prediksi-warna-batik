class Collection:

    def color_properties(color_txt):
        
        data_properties = {
            'yellow' : {
                'hex' : '#F9E571',
                'rgb' : [249, 229, 113],
                'idn' : 'Kuning'
            },

            'orange' : {
                'hex' : '#EF2C32',
                'rgb' : [239, 44, 50],
                'idn' : 'Oranye'
            },
            
            'red' : {
                'hex' : '#ED2134',
                'rgb' : [237, 33, 52],
                'idn' : 'Merah'
            },

            'brown' : {
                'hex' : '#9D4E3B',
                'rgb' : [157, 78, 59],
                'idn' : 'Cokelat'
            },

            'blue' : {
                'hex' : '#0F225C',
                'rgb' : [15, 34, 92],
                'idn' : 'Biru'
            },

            'green' : {
                'hex' : '#103F39',
                'rgb' : [16, 63, 57],
                'idn' : 'Hijau'
            },

            'purple' : {
                'hex' : '#9F2A39',
                'rgb' : [159, 42, 57],
                'idn' : 'Ungu'
            },

            'violet' : {
                'hex' : '#351B49',
                'rgb' : [53, 27, 73],
                'idn' : 'Violet'
            }
        }

        return data_properties[color_txt]
    

    def mixed_color_hex(colors_pair):

        pair_properties = {
            'yellow_yellow' : '#F5CB4B',
            'yellow_orange' : '#EE2520',
            'yellow_red' : '#F11825',
            'yellow_brown' : '#A45139',
            'yellow_blue' : '#10FF37',
            'yellow_green' : '#2B553F',
            'yellow_purple' : '#C34046',
            'yellow_violet' : '#754E4D',
            'orange_yellow' : '#F03A32',
            'orange_orange' : '#F32128',
            'orange_red' : '#F0141E',
            'orange_brown' : '#8E2A1F',
            'orange_blue' : '#15131C',
            'orange_green' : '#231A1E',
            'orange_purple' : '#A42A20',
            'orange_violet' : '#6B4E4D',
            'red_yellow' : '#EA2A2B',
            'red_orange' : '#EA261E',
            'red_red' : '#E71B1E',
            'red_brown' : '#872A20',
            'red_blue' : '#151223',
            'red_green' : '#1A1719',
            'red_purple' : '#BD3123',
            'red_violet' : '#74262A',
            'brown_yellow' : '#F19148',
            'brown_orange' : '#EC2E25',
            'brown_red' : '#EC272E',
            'brown_brown' : '#8C4230',
            'brown_blue' : '#112045',
            'brown_green' : '#252421',
            'brown_purple' : '#792C28',
            'brown_violet' : '#552728',
            'blue_yellow' : '#10213F',
            'blue_orange' : '#1C141F',
            'blue_red' : '#20121F',
            'blue_brown' : '#13131E',
            'blue_blue' : '#131231',
            'blue_green' : '#111729',
            'blue_purple' : '#18152C',
            'blue_violet' : '#11142C',
            'green_yellow' : '#1C4331',
            'green_orange' : '#1E1419',
            'green_red' : '#2D181E',
            'green_brown' : '#282423',
            'green_blue' : '#111624',
            'green_green' : '#101F1F',
            'green_purple' : '#241E26',
            'green_violet' : '#0C1523',
            'purple_yellow' : '#B2383F',
            'purple_orange' : '#9E2A20',
            'purple_red' : '#B32E1F',
            'purple_brown' : '#762824',
            'purple_blue' : '#13142B',
            'purple_green' : '#15141C',
            'purple_purple' : '#902728',
            'purple_violet' : '#141017',
            'violet_yellow' : '#755152',
            'violet_orange' : '#4A1D20',
            'violet_red' : '#6B2227',
            'violet_brown' : '#4D2327',
            'violet_blue' : '#101634',
            'violet_green' : '#141E27',
            'violet_purple' : '#321927',
            'violet_violet' : '#151222'
        }

        return pair_properties[colors_pair]


class Conversion:
    
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

