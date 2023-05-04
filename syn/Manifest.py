target = "xilinx"
action = "synthesis"
language = "verilog"

syn_device = "xc7a35t"
syn_grade = "-1"
syn_package = "ftg256"

syn_top = "KiwiSDR"
syn_project = "KiwiSDR.xpr"

syn_tool = "vivado"

include_dirs = ["../verilog", "../verilog/rx"]

modules = { "local" : [
            "../verilog",
            "../verilog/gps",
            "../verilog/ip",
            "../verilog/rx",
            "../verilog/support",
            "../verilog.Vivado.2022.2.ip"
            ]
           }
