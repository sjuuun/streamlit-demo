import streamlit as st

from stats.frequentist import calculate_z_test


def main():
    stat_sig_type = st.sidebar.radio(
        "What kind of Statistical Significance?",
        ["z-test"],
    )

    if stat_sig_type == "z-test":
        z_test()


def z_test():
    with st.container():
        st.title("Calculate Z-Test")

    with st.container():
        st.header("Input")
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Control Group")
            n_c = st.number_input(label="Total Users", min_value=1, value=5000, step=1, format="%d", key="n_c")
            conversion_c = st.number_input(label="Conversions", min_value=1, value=700, step=1, format="%d",
                                           key="conversion_c")

        with col2:
            st.subheader("Variant Group")
            n_v = st.number_input(label="Total Users", min_value=1, value=5000, step=1, format="%d", key="n_v")
            conversion_v = st.number_input(label="Conversions", min_value=1, value=800, step=1, format="%d",
                                           key="conversion_v")

        confidence = st.select_slider(
            "Select Confidence",
            options=[0.9, 0.95, 0.99],
            format_func=format_confidence
        )
    st.markdown("---")

    result = calculate_z_test(n_c, conversion_c, n_v, conversion_v)
    cvr_c = result.get("cvr_c")
    cvr_v = result.get("cvr_v")
    cvr_change = result.get("cvr_change")
    cvr_relative_change = result.get("cvr_relative_change")

    z_score = result.get("z_score")
    p_value = result.get("p_value")
    stat_sig = result.get("stat_sig")
    is_statistically_significant = stat_sig >= confidence
    is_increase = (cvr_v - cvr_c) >= 0

    with st.container():
        st.subheader("Result")
        st.markdown(f"""
        |                   | Control           | Variant           |
        |----------------   | -------------     | -------------	    |
        | Total Users	    | {n_c}	            | {n_v}	            |
        | Conversions       | {conversion_c}    | {conversion_v}    |
        | Conversion rate 	| {cvr_c:.2%}  	    | {cvr_v:.2%}  	    |
        """)

    st.markdown("---")

    with st.container():
        result_statement = ""
        if is_statistically_significant and is_increase:
            result_statement = "Significantly Increase"
        elif is_statistically_significant and not is_increase:
            result_statement = "Significantly Decrease"
        else:
            result_statement = "Not Statistically Significant"
        st.subheader(f"{result_statement}")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.metric(
                label="Conversion",
                value=f"{cvr_v:.2%}",
                delta=f"{cvr_relative_change:.2f}"
            )
        with col2:
            st.metric(
                label="Z Score",
                value=f"{z_score:.3f}"
            )
        with col3:
            st.metric(
                label="P Value",
                value=f"{p_value:.3f}"
            )


def format_confidence(c: float) -> str:
    return f"{c:.0%}"


if __name__ == "__main__":
    st.set_page_config(
        page_title="stat sig",
        page_icon="📊",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            "About": "Calculate Statistical Significance"
        }
    )
    main()
