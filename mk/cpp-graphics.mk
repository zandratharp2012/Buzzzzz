ifeq ($(PLATFORM), Mac)
	CXXFLAGS += -I/usr/local/include
    CXXFLAGS += -Wno-deprecated-declarations
	LFLAGS += -framework OpenGL -framework GLUT
	LFLAGS += -lGLUT
endif
ifeq ($(PLATFORM), Windows)
	CXXFLAGS += -I\tools\freeglut\include -Iinclude
	LFLAGS += -L\tools\freeglut\lib\x64
	LFLAGS += -lfreeglut -lglu32 -lopengl32 -Wl,--subsystem,windows
endif
ifeq ($(PLATFORM), Linux)
	CXXFLAGS += -I/usr/include -Iinclude
	LFLAGS += -lGL -l GLU -lglut
endif
