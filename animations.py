from manimlib import *

class Introduction(Scene):

    def construct(self):

        title = Text("COVID-19 Primers")
        self.play(Write(title))
        self.play(FadeOut(title))

class Introduction_Questions(Scene):

    def construct(self):

        qu_1 = Text("Can I be reinfected?")
        qu_2 = Text("What is a variant?")
        qu_3 = Text("Should we be worried about new variants?")

        questions = VGroup(qu_1, qu_2, qu_3).set_color(BLUE_C).arrange(DOWN, aligned_edge = LEFT, buff=1)

        for qu in questions:
            self.play(Write(qu), run_time=1.4)
            self.wait(0.2)


class Introduction_CasesGraph(Scene):

    def construct(self):

        # Cases are from listed total cases here https://www.worldometers.info/coronavirus/worldwide-graphs/
        cases = [
            987, 35429, 80267, 
            137411, 624877, 1892307, 
            3227180, 4623281, 6271685,
            8298601, 10917164, 14351572, 
            18476906, 22592557, 26821979, 
            31392867,36114453, 41766661, 
            49789130, 59343810, 68848119, 
            79146413, 89462006, 99778805, 
            107360013, 113485733    
        ]

        dates = [
            "Jan 22, 2020", "Feb 07, 2020", "Feb 23, 2020",
            "Mar 10, 2020", "Mar 26, 2020", "Apr 11, 2020",
            "Apr 27, 2020", "May 13, 2020", "May 29, 2020",
            "Jun 14, 2020", "Jun 30, 2020", "Jul 16, 2020",
            "Aug 01, 2020", "Aug 17, 2020", "Sep 02, 2020",
            "Sep 18, 2020", "Oct 04, 2020", "Oct 20, 2020",
            "Nov 05, 2020", "Nov 21, 2020", "Dec 07, 2020",
            "Dec 23, 2020", "Jan 08, 2021", "Jan 24, 2021",
            "Feb 09, 2021", "Feb 25, 2021"
        ]

        axes = Axes(
            x_range = (0, 400, 16),
            y_range = (0, 120000000, 10000000),   
            axis_config = {'include_tip': False},
        )

        axes.center()
        axes.to_edge(DOWN, buff=0.8)
        axes.to_edge(LEFT, buff=0.8)

        title = Text("Cumulative worldwide COVID-19 cases", font_size=30, t2c={"COVID-19": RED})
        title.next_to(axes, UP, buff=0.5)

        # Set up dates on x axis
        x_labels = VGroup()

        for i in range(0, len(cases)):
            # If interval of 4
            if(i % 4 == 0):
                label = Text(dates[i])
                label.set_height(0.12)
                label.rotate(35 * DEGREES)
                axis_point = axes.c2p(i * 16, 0)
                label.move_to(axis_point, UR)
                label.shift(MED_SMALL_BUFF * DOWN)
                label.shift(SMALL_BUFF * RIGHT)
                x_labels.add(label)

        # Set up labels on y axis
        y_labels = VGroup()

        for i in range(0, 13):
            label = Text(f"{i * 10}M")
            label.set_height(0.12)
            axis_point = axes.c2p(0, i * 10000000)

            label.move_to(axis_point, RIGHT)
            label.shift(MED_SMALL_BUFF * LEFT)
            y_labels.add(label)


        self.play(FadeIn(axes), FadeIn(x_labels), FadeIn(y_labels), Write(title))

        dots = VGroup()

        for i, case_no in enumerate(cases):
            dot = Dot()
            dot.set_color(YELLOW)
            dot.set_height(0.075)
            dot.move_to(axes.c2p(i * 16, case_no))
            dots.add(dot)

            if(i == 0):
                case_counter = Integer(case_no, font_size=25)
                case_counter.next_to(dot, UR)

                self.play(FadeIn(dot), FadeIn(case_counter), run_time=0.3)
            else:
                self.play(FadeIn(dot), ChangeDecimalToValue(case_counter, case_no), ApplyMethod(case_counter.next_to, dot, UP), run_time=0.3)

        cases_group = VGroup()
        cases_group.add(dots, case_counter, y_labels, x_labels, axes, title)
        

        #self.play(FadeOut(cases_group))


class Introduction_PapersGraph(Scene):

    def construct(self):
        # No of papers from https://covid19primer.com/dashboard
        papers = [
            2, 470, 2224,
            9504, 21251, 33312,
            43851, 56087, 66841,
            78036, 88514, 98405,
            109385
        ]

        dates = [
            "Jan 22, 2020", "Feb 23, 2020", "Mar 26, 2020", 
            "Apr 27, 2020", "May 29, 2020", "Jun 30, 2020", 
            "Aug 01, 2020", "Sep 02, 2020", "Oct 04, 2020",
            "Nov 05, 2020",  "Dec 07, 2020", "Jan 08, 2021", 
            "Feb 09, 2021",
        ]

        axes = Axes(
            x_range = (0, 400, 32),
            y_range = (0, 110000, 10000),   
            axis_config = {'include_tip': False},
        )

        axes.center()
        axes.to_edge(DOWN, buff=0.8)
        axes.to_edge(LEFT, buff=0.8)

        title = Text("Cumulative COVID-19 research papers", font_size=30, t2c={"COVID-19": RED})
        title.next_to(axes, UP, buff=0.5)

        # Set up dates on x axis
        x_labels = VGroup()

        for i in range(0, len(papers)):

            label = Text(dates[i])
            label.set_height(0.12)
            label.rotate(35 * DEGREES)
            axis_point = axes.c2p(i * 32, 0)
            label.move_to(axis_point, UR)
            label.shift(MED_SMALL_BUFF * DOWN)
            label.shift(SMALL_BUFF * RIGHT)
            x_labels.add(label)

        # Set up labels on y axis
        y_labels = VGroup()

        for i in range(0, 12):
            label = Text(f"{i * 10}K")
            label.set_height(0.12)
            axis_point = axes.c2p(0, i * 10000)

            label.move_to(axis_point, RIGHT)
            label.shift(MED_SMALL_BUFF * LEFT)
            y_labels.add(label)


        self.play(FadeIn(axes), FadeIn(x_labels), FadeIn(y_labels), Write(title))

        dots = VGroup()

        for i, paper_no in enumerate(papers):
            dot = Dot()
            dot.set_color(YELLOW)
            dot.set_height(0.075)
            dot.move_to(axes.c2p(i * 32, paper_no))
            dots.add(dot)

            if(i == 0):
                paper_counter = Integer(paper_no, font_size=25)
                paper_counter.next_to(dot, UR)

                self.play(FadeIn(dot), FadeIn(paper_counter), run_time=0.3)
            else:
                self.play(FadeIn(dot), ChangeDecimalToValue(paper_counter, paper_no), ApplyMethod(paper_counter.next_to, dot, UP), run_time=0.3)

        paper_group = VGroup()
        paper_group.add(dots, paper_counter, y_labels, x_labels, axes, title)
        self.play(FadeOut(paper_group))


class Qu1_ReinfectionNumbers(Scene):

    def construct(self):

        reinfected = Text(
            "4 confirmed reinfections out of 115 million cases", 
            t2c = {"4": ORANGE, "115": BLUE},
            font_size=35
        )

        self.play(Write(reinfected))


class Qu1_Reinfection(Scene):

    def construct(self):
        
        # Population size + infected at end
        grids = VGroup()

        for i in range(0, 2):
            grid = Tex(r"\pi").get_grid(10, 10, height=4)
           
            grids.add(grid)

        grids.arrange_in_grid(buff=1.3)

        # Set up box labels
        label_1 = Text("Previously Infected", font_size=30)
        label_1.next_to(grids[0], UP, buff=0.4)
        label_1_bottom = Text("0.67% reinfected", font_size=20).next_to(grids[0], DOWN)

        label_2 = Text("Previously Non-Infected", font_size=30)
        label_2.next_to(grids[1], UP, buff=0.4)
        label_2_bottom = Text("2.9% infected", font_size=20).next_to(grids[1], DOWN)


        labels = VGroup()
        labels.add(label_1, label_2)

        # Display label and boxes
        self.play(Write(grids), Write(labels))

        self.wait(1)

        self.play(ApplyMethod(grids[0][0].set_color, RED), FadeIn(label_1_bottom))

        self.wait(1)

        for i in range(0, 3):
            if(i == 2):
                self.play(ApplyMethod(grids[1][i].set_color, RED), FadeIn(label_2_bottom), run_time=0.2)
            else:
                self.play(ApplyMethod(grids[1][i].set_color, RED), run_time=0.2)


        self.wait(1)

        self.play(FadeOut(labels), FadeOut(grids), FadeOut(label_1_bottom), FadeOut(label_2_bottom))

        effiacy_text = Text(
            """This equates to an 83% reduction in the risk of infection""",
            font_size=35,
            t2c={"83%": BLUE}
        )
        
        self.play(Write(effiacy_text))



class Qu1_Efficacy(Scene):
    def construct(self):

        config = {
            "height": 5,
            "width": 10,
            "max_value": 100,
            "bar_names": ["Infection", "AZ/Oxford", "Pfizer/BioNTech"],
            "bar_label_scale_val": 0.70
        }

        ve = [83, 82, 94]
        ve_ci_95 = [[76, 87], [62.7, 91.7], [87, 98]]
        ve_chart = BarChart(values=ve, **config)

        ve_title = Text("Vaccine and Infection Efficacy").next_to(ve_chart, UP, buff=0.5).scale(0.7)
        ve_y = Text("Efficacy (%)").rotate(angle=TAU/4).next_to(ve_chart, LEFT, buff=0.3).scale(0.6)

        self.play(Write(ve_chart), Write(ve_y), Write(ve_title))


class Qu1_EfficacyText(Scene):

    def construct(self):
        text = Text("All provide a significant reduction in the risk of infection", font_size=30, t2c={"significant": BLUE})
        self.play(Write(text))

        self.play(FadeOut(text))

class Qu1to2Transition(Scene):

    def construct(self):

        title = Text("Should we worry about new variants?")
        self.play(Write(title))

        new_title = Text("What is a variant?")
        self.play(Transform(title, new_title))

        
class Qu2_Introduction(Scene):

    def construct(self):
        
        variant_def = Text("A virus whose genomic sequence varies from that of the reference virus", font_size=30, t2c={"varies": BLUE, "reference": ORANGE})

        self.play(Write(variant_def), run_time=4)

        self.play(FadeOut(variant_def))

        reference_title = Text("SARS-CoV-2 Wuhan-Hu-1 Isolate", font_size=30, color=BLUE)
        reference_title.to_edge(UP, buff=0.4)
        reference_subtitle = Text("(Reference Genome)", font_size=25, color=BLUE).next_to(reference_title, DOWN, buff=0.3)

        self.play(FadeIn(reference_title), FadeIn(reference_subtitle))

        bases = {"A": GREEN, "T": RED, "C": BLUE, "G": ORANGE}

        lines = VGroup()
        line_1 = Text("ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTC", font_size=30, t2c=bases).next_to(reference_subtitle, DOWN, buff=0.8)
        line_2 = Text("GATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGT", font_size=30, t2c=bases).next_to(line_1, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_3 = Text("GGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAA", font_size=30, t2c=bases).next_to(line_2, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_4 = Text("TTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTC", font_size=30, t2c=bases).next_to(line_3, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_5 = Text("TTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTC", font_size=30, t2c=bases).next_to(line_4, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_6 = Text("TATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCG", font_size=30, t2c=bases).next_to(line_5, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_7 = Text("ATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGT", font_size=30, t2c=bases).next_to(line_6, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_8 = Text("AAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACG", font_size=30, t2c=bases).next_to(line_7, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_9 = Text("TCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTA", font_size=30, t2c=bases).next_to(line_8, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_10 = Text("CGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCAC", font_size=30, t2c=bases).next_to(line_9, DOWN, buff=0.15).align_to(line_1, LEFT)
        line_11 = Text("...", font_size=30).next_to(line_10, DOWN, buff=0.5)
        lines.add(line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11)
        self.play(Write(lines))
        self.embed()


class Qu2_BarChart(Scene):

    def construct(self):

        config = {
            "height": 5,
            "width": 10,
            "max_value": 400,
            "bar_names": ["", ""],
            "bar_label_scale_val": 0.70
        }

        aa_subs = [380, 17]
        chart = BarChart(values=aa_subs, **config)
        chart.to_edge(DOWN, buff=1.1)


        strain_def = Text("A variant that possess new, unique and stable characteristics", t2c={"new": ORANGE, "unique": ORANGE, "stable": ORANGE}, font_size=30)

        self.play(Write(strain_def), run_time=3)
        
        label_1 = Text("SARS-CoV-2", font_size=20).next_to(chart.bars[0], DOWN)
        label_2 = Text("vs", font_size=20).next_to(label_1, DOWN)
        label_3 = Text("SARS-CoV", font_size=20).next_to(label_2, DOWN)

        bar_1 = VGroup()
        bar_1.add(label_1, label_2, label_3)

        label_4 = Text("P.1 Variant", font_size=20).next_to(chart.bars[1], DOWN)
        label_5 = Text("vs", font_size=20).next_to(label_4, DOWN)
        label_6 = Text("Reference", font_size=20).next_to(label_5, DOWN)
    
        bar_2 = VGroup()
        bar_2.add(label_4, label_5, label_6)

        y_axis = Text("Amino acid differences", font_size=25).rotate(90*DEGREES)
        y_axis.next_to(chart, LEFT, buff=0.8)

        title = Text("Amino acid differences between different viruses", font_size=25).next_to(chart, UP, buff=0.5)
        self.play(FadeOut(strain_def))
        self.play(Write(chart), FadeIn(bar_1), FadeIn(bar_2), FadeIn(y_axis), FadeIn(title))


class Qu3_Introduction(Scene):

    def construct(self):
        
        main_title = Text("Should we worry about variants?", color=BLUE_C)
        self.play(Write(main_title))

        short_term = Text("Short Term", font_size=50).shift(UP)
        long_term = Text("Long Term", font_size=50).next_to(short_term, DOWN, buff=1)
        
        self.play(ApplyMethod(main_title.shift, UP * 3))
        self.play(Write(short_term), Write(long_term))

        self.embed()

class Qu3_ShortTerm(Scene):

    def construct(self):
        
        main_title = Text("Should we worry about variants?", color=BLUE_C).shift(UP * 3)

        short_term = Text("Short Term", font_size=50).shift(UP)
        long_term = Text("Long Term", font_size=50).next_to(short_term, DOWN, buff=1)
        
        self.play(Write(main_title))
        self.play(FadeIn(short_term))
        self.play(FadeIn(long_term))
       

        self.play(FadeOut(main_title), FadeOut(long_term))
        self.play(ApplyMethod(short_term.to_corner, UL))

        grid = Tex(r"\pi").get_grid(10, 10, height=3)
        grid[0][0].set_color(BLUE)
        label_1 = Text("Susceptible Population", font_size=25)
        label_1.next_to(grid, UP, buff=0.4)
        label_1_bottom = Text("Blue = immunity", font_size=20).next_to(grid, DOWN)


        grid_objects = VGroup()
        grid_objects.add(grid, label_1, label_1_bottom)

        self.play(FadeIn(grid_objects))
    
        plus = Text("+", font_size=45, color=RED)

        self.play(ApplyMethod(grid_objects.shift, LEFT * 3), FadeIn(plus))

        arrow = Arrow(DOWN, UP)
        arrow_text = Text("Increased Transmissibility", font_size=25).next_to(arrow, RIGHT, buff=0.75)

        arrow_objects = VGroup()
        arrow_objects.add(arrow, arrow_text)
        arrow_objects.shift(RIGHT)

        self.play(FadeIn(arrow_objects))

        everything = VGroup()
        everything.add(arrow_objects, grid_objects, plus)

        equals = Text("=", font_size=45, color=RED).to_edge(LEFT, buff=0.8)

        self.play(Transform(everything, equals))

        infections_arrow = Arrow(DOWN, UP)
        infections_text = Text("More Cases", font_size=23).next_to(infections_arrow, RIGHT, buff=0.5)
        infections = VGroup()
        infections.add(infections_arrow, infections_text).next_to(equals, RIGHT)
        eq_1 = Text("=", font_size=45, color=RED).next_to(infections, RIGHT)

        hospitilizations_arrow = Arrow(DOWN, UP)
        hospitilizations_text = Text("More Hospitilizations", font_size=23).next_to(hospitilizations_arrow, RIGHT, buff=0.5)
        hospitilizations = VGroup().add(hospitilizations_arrow, hospitilizations_text).next_to(eq_1, RIGHT)
        eq_2 = Text("=", font_size=45, color=RED).next_to(hospitilizations, RIGHT)


        deaths_arrow = Arrow(DOWN, UP)
        deaths_text = Text("More Deaths", font_size=23).next_to(deaths_arrow, RIGHT, buff=0.5)
        deaths = VGroup().add(deaths_arrow, deaths_text).next_to(eq_2, RIGHT)


        self.play(FadeIn(infections))
        self.play(FadeIn(eq_1))
        self.play(FadeIn(hospitilizations))
        self.play(FadeIn(eq_2))
        self.play(FadeIn(deaths))

        self.play(FadeOut(infections), FadeOut(eq_1), FadeOut(hospitilizations), FadeOut(eq_2), FadeOut(deaths), FadeOut(equals), FadeOut(everything))


        arrow = Arrow(DOWN, UP)
        arrow.shift(RIGHT * 2)
        arrow_text = Text("Increased Transmissibility", font_size=25).next_to(arrow, RIGHT, buff=0.75)

        self.play(FadeIn(arrow), FadeIn(arrow_text))        

        self.play(FadeOut(arrow), FadeOut(arrow_text))


class Qu3_LongTerm(Scene):

    def construct(self):


        short_term = Text("Short Term", font_size=50).to_corner(UL)
        long_term = Text("Long Term", font_size=50).to_corner(UL)
        self.add(short_term)

        self.play(Transform(short_term, long_term))

        plus = Text("+", color=RED, font_size=45).shift(LEFT * 3)
        self.play(FadeIn(plus))

        text = Text("= Resistant to neutralizing antibodies", font_size=25).shift(RIGHT * 4)
        self.play(Write(text))

        self.play(FadeOut(text), FadeOut(plus), FadeOut(long_term), FadeOut(short_term))
        # Add in here
        title = Text("Antibodies", font_size=25).shift(UP *3).shift(LEFT * 3)
        virus = ImageMobject("sars-cov-2.png").next_to(title, DOWN, buff=2.0)
        antibody = SVGMobject("antibody.svg").scale(0.4).to_corner(UL).rotate(225 * DEGREES)

        self.play(FadeIn(title), FadeIn(virus))

        self.play(FadeIn(antibody))
        self.play(ApplyMethod(antibody.shift, RIGHT * 1.50 + DOWN * 2.65))

        title_2 = Text("T Cells", font_size=25).shift(UP * 3).shift(RIGHT * 3)
        infected_cell = ImageMobject("infected-cell.png").next_to(title_2, DOWN, buff=2.0)
        t_cell = ImageMobject("t-cell.png").scale(0.3).to_corner(UR).rotate(139 * DEGREES)

        self.play(FadeIn(title_2), FadeIn(infected_cell))
        self.play(FadeIn(t_cell))
        self.play(ApplyMethod(t_cell.shift, LEFT * 2 + DOWN * 2.01))



class Qu3_Preprint(Scene):

    def construct(self):
        text = Text("= Negligible impact on T cell response", font_size=25).shift(RIGHT * 4)
        self.play(Write(text))

        self.play(FadeOut(text))


class Qu3_TCell(Scene):

    def construct(self):

        text = Text("T Cells therefore:").to_edge(TOP)
        qu_1 = Text("Do not prevent infection", t2c={"not": RED})
        qu_2 = Text("BUT do reduce the severity of infection", t2c={"reduce": BLUE})

        questions = VGroup(qu_1, qu_2).arrange(DOWN, aligned_edge = LEFT, buff=0.4)

        self.play(Write(text))
        self.play(Write(qu_1))
        self.play(Write(qu_2))

class Qu3_VaccineStatement(Scene):

    def construct(self):

        text = Text("Vaccination or prior immunity is likely to reduce disease severity", t2c={"reduce": BLUE}, font_size=25)
        self.play(Write(text))

class Outro(Scene):

    def construct(self):

        title = Text("To summarise:").shift(UP * 3)

        qu_1 = Text("Reinfection is likely to be very rare", font_size=25, t2c={"very rare": BLUE})
        qu_2 = Text("A variant is a virus whose genomic sequence varies from that of the reference virus", font_size=25, t2c={"varies": BLUE, "reference": ORANGE})
        qu_3 = Text("In the long-term, in vaccinated populations, variants are unlikely to be a significant threat", font_size=25, t2c={"unlikely": BLUE})

        questions = VGroup(qu_1, qu_2, qu_3).arrange(DOWN, aligned_edge = LEFT, buff=0.5)

        self.play(Write(title))
        for qu in questions:
            self.play(Write(qu), run_time=1.4)
            self.wait(0.2)

